# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input("anna tuumat: "))
while True:
        if tuumat >= 0:
                print(f"{tuumat * 2.54} cm")
                tuumat = float(input("anna tuumat: "))
        if tuumat < 0:
                print(f"virheellinen tuumamäärä")
                break