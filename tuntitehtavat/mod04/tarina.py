hahmo = input("hahmon nimi: ")

print(f"hei {hahmo}, valitaan kahden väri väliltä.")
asu = int(input("valitaanko 1: keltainen väri vai 2: punainen väri? "))

if asu == 1:
    print("hieno valinta! keltainen sopii elokuuhun.")
if asu == 2:
    print("hieno valinta! punainen sopii auringonlaskuun.")
elif asu != 1 and asu != 2:
    print("tämä väri ei ole juuri nyt käytettävissä.")