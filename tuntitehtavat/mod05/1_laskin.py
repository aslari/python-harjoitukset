# luo laskin, joka tekee laskutoimituksia kunnes käyttäjä päättää lopettaa.
# laskin tulostaa käyttäjälle valikon, josta valitaan plus, miinus, kertolasku tai lopetus
# jos käyttäjä ei valitse lopetusta, laskin pyytää kahta numeroa ja tulostaa tuloksen
# laskin tulostaa valikon uudestaan, ja käyttäjä voi valita uuden laskutoimituksen

valikko = input("valitse toiminto: +, -, *, stop: ")

while valikko != "stop":
    print(f"laskutoimitus: ")
    one = int(input("anna eka numero: "))
    two = int(input("anna toka numero: "))
    if valikko == "+":
        print(f"{one} + {two} = {one+two}")
    if valikko == "-":
        print(f"{one} - {two} = {one-two} ")
    if valikko == "*":
        print(f"{one} * {two} = {one*two} ")
    valikko = input("valitse toiminto: +, -, *, stop: ")