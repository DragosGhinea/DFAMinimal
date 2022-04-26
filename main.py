import AutomatDeterminist as DFA

with open("minimal2.in") as f:
    automat = DFA.AutomatDeterminist()
    for stare in f.readline().split():
        automat.adaugaStare(stare)

    for litera in f.readline().split():
        automat.adaugaLitera(litera)

    nrTranzitii = int(f.readline())
    while nrTranzitii:
        stareStart, stareFinal, litera = f.readline().split()
        automat.adaugaTranzitie(stareStart, stareFinal, litera)
        nrTranzitii -= 1

    automat.seteazaStareInitiala(f.readline().strip())
    for stareF in f.readline().split():
        automat.adaugaStareFinala(stareF)

    minimal = automat.genereazaAutomatMinimal()
    minimal.afisare()

# -----minimal.in-------
# nume stari separate prin spatiu
# literele alfabetului separate prin spatiu
# numar tranzitii n
# n linii de tranzitii de forma (nod start, not destinatie, litera)
# stare initiala
# stari finale
