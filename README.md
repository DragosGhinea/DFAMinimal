
# DFA Minimal | Implementare

In **AutomatDeterminist.py** am implementat clasa cu acelasi nume care dispune de mai multe metode.

  - adaugaStare(stare)
  - stergeStare(stare)
  - adaugaLitera(litera)
  - stergeLitera(litera)
  - adaugaTranzitie(stareStart, stareDestinatie, litera)
  - stergeTranzitie(stareStart, litera)
  - seteazaStareInitiala(stare)
  - adaugaStareFinala(stare)
  - stergeStareFinala(stare)
  - stariInaccesibile()
  - transformaComplet()
  - genereazaAutomatMinimal()
  - afisare()

## Generalitati

Automatul se initializeaza fara niciun parametru si trebuie ca starile si tranzitiile dintre acestea sa fie adaugate prin intermediul metodelor de **adaugaStare** si **adaugaTranzitie**.

Automatul nu poate testa cuvinte ci este folosit doar pentru incapsulare, in vederea prelucrarii acestuia (transformarea in automat minimal).


## Metode

### » adaugaStare(stare)
Descriere: Adauga o stare in automat.

### » stergeStare(stare)
Descriere: Sterge o stare si tranzitiile asociate acesteia. Returneaza False daca starea nu exista si True daca aceasta a fost stearsa cu succes.

### » adaugaLitera(litera)
Descriere: Adauga o litera in alfabetul automatului.

### » stergeLitera(litera)
Descriere: Sterge o litera din alfabetul automatului. Returneaza False daca litera nu exista si True daca aceasta a fost stearsa cu succes.

### » seteazaStareInitiala(stare)
Descriere: Seteaza starea initiala a automatului. Returneaza True daca aceasta exista, False in caz contrar.

### » adaugaStareFinala(stare)
Descriere: Adauga o stare in lista starilor finale ale automatului, daca aceasta exista. Returneaza True daca starea exista si False in caz contrar.

### » stergeStareFinala(stare)
Descriere: Daca o stare este in lista starilor finale aceasta va fi eliminata din lista si metoda va returna True, False in cazul in care starea nu se regaseste in lista.

### » adaugaTranzitie(stareStart, stareDestinatie, tranzitie)
Descriere: Adauga o tranzitie de la starea **stareStart** catre starea **stareDestinatie** cu valoarea **tranzitie**. Returneaza False daca starile nu au fost gasit, True in caz contrar.

### » stergeTranzitie(stareStart, tranzitie)
Descriere: Sterge o tranzitie de la starea **stareStart** cu valoarea **tranzitie**. Returneaza True daca tranzitia a fost stearsa cu succes, False in orice alt caz. Precizarea starii destinatie nu este necesar, intrucat este un automat determinist.

### » stariInaccesibile()
Descriere: In vederea minimizarii automatului se identifica starile la care nu se poate ajunge plecand din starea initiala. Daca starea initiala nu este setata, metoda returneaza toate starile.

### » transformaComplet()
Descriere: Tot in vederea minimizarii, automatul trebuie sa fie complet pentru a putea compara starile.

### » genereazaAutomatMinimal()
Descriere: Returneaza un nou automat, cel care rezulta din minimizare.

### » afisare()
Descriere: Afiseaza mai multe informatii despre automat precum starile, alfabetul, starea initiala si cele finale, tranzitiile si numarul acestora.

# DFA Minimal | Exemplu Input

In **minimal.in** avem urmatorul input:
```python
a b c d e f #starile automatului
0 1 #alfabetul automatului
12 #numarul de tranzitii
a b 0 #tranzitie sub forma (stareStart, stareDestinatie, tranzitie)
b a 0 #...
a c 1 #...
b d 1 #...
c e 0 #...
c f 1 #...
d e 0 #...
d f 1 #...
e e 0 #...
e f 1 #...
f f 0 #...
f f 1 #tranzitie sub forma (stareStart, stareDestinatie, tranzitie)
a #starea initiala
c d e #starile finale
```

Automatul din inputul anterior:
![AutomatIMG](https://github.com/DragosGhinea/DFAMinimal/blob/main/automat1.png)

Automatul minimal asociat celui de mai sus:
![AutomatMinimalIMG](https://github.com/DragosGhinea/DFAMinimal/blob/main/automatM1.png)

## Exemplu 2
Automatul din **minimal2.in**:
![Automat2IMG](https://github.com/DragosGhinea/DFAMinimal/blob/main/automat2.png)

Automatul minimal asociat celui de mai sus:
![AutomatMinimal2IMG](https://github.com/DragosGhinea/DFAMinimal/blob/main/automatM2.png)
