# Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

luku = 1

while True:
    if luku >= 1 and luku <= 1000 and luku % 3 == 0:
        print(f"{luku}")
        luku = luku + 1
    else:
        luku = luku + 1