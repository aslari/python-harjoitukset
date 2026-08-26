# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet
# ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("anna vuosi: "))

if (vuosi % 4 == 0) and (vuosi % 100 != 0):
    print("on karkausvuosi")

elif (vuosi % 4 == 0) and (vuosi % 100 == 0) and (vuosi % 400 == 0):
    print("on karkausvuosi")


elif (vuosi % 4 == 0) and vuosi % 100 == 0 and not vuosi % 400 == 0:
    print("ei ole karkausvuosi")

else:
    print("ei ole karkausvuosi")