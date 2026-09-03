# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden
# lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita
# ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random
nopat = []
noppa = int(input("anna noppien määrä: "))
heitot = 0
while noppa > heitot:
    uusnoppa = random.randint(1,6)
    print(f"heitettiin {uusnoppa}")
    nopat.append(uusnoppa)
    heitot = heitot + 1

yht = 0
if noppa == heitot:
    for numero in nopat:
        yht += numero
    print(f"noppien summa: {yht}")
