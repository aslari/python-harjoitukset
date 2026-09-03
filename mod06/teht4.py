# Kirjoita ohjelma, joka kysyy käyttäjältä viiden
# kaupungin nimet yksi kerrallaan (käytä
# for-toistorakennetta nimien kysymiseen) ja tallentaa
# ne listarakenteeseen. Lopuksi ohjelma tulostaa
# kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja
# for/in toistorakennetta niiden läpikäymiseen.

kaupungit = ["kaupunkilista:"]
for n in kaupungit:
    kaupungit.append(input("anna 1. kaupungin nimi: "))
    kaupungit.append(input("anna 2. kaupungin nimi: "))
    kaupungit.append(input("anna 3. kaupungin nimi: "))
    kaupungit.append(input("anna 4. kaupungin nimi: "))
    kaupungit.append(input("anna 5. kaupungin nimi: "))
    break
#print("syötetyt kaupungit:")
for n in kaupungit:
    print(f"{n}")