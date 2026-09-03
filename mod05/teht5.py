#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen
# ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
# tunnus ja salasana kysytään uudelleen. Tätä jatketaan
# kunnes kirjautumistiedot ovat oikein tai väärät tiedot on
# syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan
# Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea
# käyttäjätunnus on python ja salasana rules).

tunnus = "python"
salasana = "rules"
yritys = 0

while True:
    yritys = yritys + 1
    kysy_tunnus = input("anna käyttäjätunnus: ")

    kysy_salasana = input("anna salasana: ")
    if yritys == 5:
        print("pääsy evätty. ")
        break
    elif tunnus != kysy_tunnus or salasana != kysy_salasana:
        yritys = yritys + 1
        kysy_tunnus = input("anna käyttäjätunnus: ")
        kysy_salasana = input("anna salasana: ")
    if tunnus == kysy_tunnus and salasana == kysy_salasana:
        print("tervetuloa! ")
        break