nimi = input("pelaajan nimi: ")
ika = int(input("pelaajan ikä: "))

if ika > 12:
    print(f"tervetuloa! nimi: {nimi} ja ikä {ika} vuotta")
    komento = input("anna komento: 1 info / 2 tervehdys / 3 vaihda tunnuksia / 4 lopeta: ")
    while komento != "4":
        if komento == "1":
            print("pelin info: Kaninkolo")
            komento = input("anna komento: 1 info / 2 tervehdys / 3 vaihda tunnuksia / 4 lopeta: ")
        elif komento == "2":
            print(f"hei, {nimi}!")
            komento = input("anna komento: 1 info / 2 tervehdys / 3 vaihda tunnuksia / 4 lopeta: ")
        elif komento == "3":
            nimi = input("pelaajan nimi: ")
            print(f"info vaihdettu, {nimi}")
            komento = input("anna komento: 1 info / 2 tervehdys / 3 vaihda tunnuksia / 4 lopeta: ")
    else:
        print("---- SHUTTING DOWN ----")
while ika <= 12:
    print("---- ACCESS DENIED ----")
    break