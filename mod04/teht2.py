# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan
# luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#    LUX on parvekkeellinen hytti yläkannella.
#    A on ikkunallinen hytti autokannen yläpuolella.
#    B on ikkunaton hytti autokannen yläpuolella.
#    C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma
# tulostaa Virheellinen hyttiluokka.

hytti = input("anna hyttiluokka: ")
print("tässä kuvaus:")

if hytti == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif hytti == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hytti == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")