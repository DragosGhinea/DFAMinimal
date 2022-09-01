import copy


class AutomatDeterminist:
    def __init__(self):
        self.stari = set()
        self.alfabet = set()
        self.stareInitiala = None
        self.stariFinale = set()
        self.tranzitii = {}

    def adaugaStare(self, stare):
        if stare in self.stari:
            return False

        self.stari.add(stare)
        return True

    def stergeStare(self, stare):
        if stare not in self.stari:
            return False

        self.stari.remove(stare)
        self.tranzitii.pop(stare)
        if self.stareInitiala == stare:
            self.stareInitiala = None
        self.stariFinale.remove(stare)
        for tranzitiiLocale in self.tranzitii.values():
            for litera, stareD in tranzitiiLocale.items():
                if stareD == stare:
                    tranzitiiLocale.pop(litera)
        return True

    def adaugaLitera(self, litera):
        if litera in self.alfabet:
            return False

        self.alfabet.add(litera)
        return True

    def stergeLitera(self, litera):
        if litera not in self.alfabet:
            return False

        self.alfabet.remove(litera)
        return True

    def adaugaTranzitie(self, stareStart, stareDestinatie, litera):
        if stareStart not in self.stari:
            return False
        if stareDestinatie not in self.stari:
            return False
        if litera not in self.alfabet:
            return False

        tranzitiiLocale = self.tranzitii.get(stareStart, {})
        tranzitiiLocale[litera] = stareDestinatie
        self.tranzitii[stareStart] = tranzitiiLocale
        return True

    def stergeTranzitie(self, stareStart, litera):
        if stareStart not in self.stari:
            return False
        if litera not in self.alfabet:
            return False

        if stareStart in self.tranzitii:
            self.tranzitii[stareStart].pop(litera)
        return True

    def seteazaStareInitiala(self, stare):
        if stare not in self.stari:
            return False

        self.stareInitiala = stare
        return True

    def adaugaStareFinala(self, stare):
        if stare not in self.stari or stare in self.stariFinale:
            return False

        self.stariFinale.add(stare)
        return True

    def stergeStareFinala(self, stare):
        if stare not in self.stariFinale:
            return False

        self.stariFinale.remove(stare)
        return True

    def stariInaccesibile(self):
        if self.stareInitiala is None:
            return self.stari

        stariAccesibile = set(self.stareInitiala)
        stariNoi = set(self.stareInitiala)

        while len(stariNoi) != 0:
            temp = set()
            for stare in stariNoi:
                for litera in self.alfabet:
                    dest = self.tranzitii.get(stare, {}).get(litera, None)
                    if dest is not None:
                        temp.add(dest)
            stariNoi = temp - stariAccesibile
            stariAccesibile = stariAccesibile | stariNoi

        return self.stari - stariAccesibile

    def transformaComplet(self):
        eComplet = True
        for stare in self.stari:
            if stare in self.stari:
                for litera in self.alfabet:
                    if litera not in self.tranzitii[stare]:
                        eComplet = False
                        self.stari[stare][litera] = 'sink'
            else:
                for litera in self.alfabet:
                    self.stari[stare][litera] = 'sink'

        if eComplet is False:
            self.stari.add('sink')
            for litera in self.alfabet:
                self.stari['sink'][litera] = 'sink'

    def genereazaAutomatMinimal(self):
        automat = copy.deepcopy(self)

        for stare in automat.stariInaccesibile():
            automat.stergeStare(stare)

        automat.transformaComplet()  # Pentru a putea compara starile mai tarziu, trebuie ca toate literele sa aiba destinatii

        MulIndex = {}  # Pentru fiecare litera, tine minte in ce multime se afla
        multimi = [list(automat.stari - automat.stariFinale), list(automat.stariFinale)]

        for stare in automat.stariFinale:
            MulIndex[stare] = 1

        for stare in automat.stari - automat.stariFinale:
            MulIndex[stare] = 0

        while True:
            marime = len(multimi)
            for multime in multimi:
                if len(multime) > 1:
                    destinatiiM = {}
                    for litera in automat.alfabet:
                        destinatiiM[litera] = MulIndex[
                            automat.tranzitii[multime[0]][litera]]  # Pentru prima stare din multime
                        # obtinem destinatiile fiecarei litere

                    for stare in multime[1:]:  # Verificam traseul starilor comparativ cu prima stare din multime
                        for litera in automat.alfabet:
                            stareDestinatie = automat.tranzitii[stare][litera]
                            if MulIndex[stareDestinatie] != destinatiiM[litera]:  # Daca destinatia se afla altundeva
                                # comparat cu primul element din multime,
                                # il mutam intr-o multime noua

                                MulIndex[stare] = marime  # Noul index
                                multime.remove(stare)  # Nu mai face parte din vechea multime
                                if len(multimi) == marime:  # Daca inca nu exista multimea noua, o initializam cu primul element
                                    multimi.append([stare])
                                else:  # Daca exista, doar adaugam noua stare gasita la ea
                                    multimi[-1] += stare
                                break
            if marime == len(multimi):  # Daca multimile curente nu au mai fost sparte in multimi noi ne oprim
                break

        deReturnat = AutomatDeterminist()  # initializam automatul minimal
        stari = [",".join(sorted(m)) for m in multimi]  # unim starile pastrand pozitiile

        for stare in stari:
            deReturnat.adaugaStare(stare)

        deReturnat.alfabet = automat.alfabet

        for stare in multimi:
            for litera in automat.alfabet:
                # Deoarece sunt echivalente, pentru fiecare multime, adaugam tranzitiile in functie de prima stare
                deReturnat.adaugaTranzitie(stari[MulIndex[stare[0]]],
                                           stari[MulIndex[automat.tranzitii[stare[0]][litera]]], litera)

        deReturnat.seteazaStareInitiala(stari[MulIndex[automat.stareInitiala]])

        for stare in automat.stariFinale:
            deReturnat.adaugaStareFinala(stari[MulIndex[stare]])

        return deReturnat

    def afisare(self):
        print("Stari: (", " ) ( ".join(self.stari), ")")
        print("Stare Initiala:", self.stareInitiala)
        print("Stari Finale: (", " ) ( ".join(self.stariFinale), ")")
        print("Alfabet:", *self.alfabet)

        numarTranzitii = 0
        for local in self.tranzitii.values():
            numarTranzitii += len(local)

        print("Numar tranzitii:", numarTranzitii)
        for stareStart, tranzitiiLocale in self.tranzitii.items():
            for litera, stareDestinatie in tranzitiiLocale.items():
                print(stareStart, "---", litera, "--->", stareDestinatie)
