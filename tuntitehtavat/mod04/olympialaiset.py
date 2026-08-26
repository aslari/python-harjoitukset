# onko olympiavuosi?
# olympialaiset aina neljällä jaollisina vuosina (esim. 2000, 2004, ...)

vuosi = int(input("anna vuosi: "))
if vuosi % 4 == 0:
    print("oli olympiavuosi")
if vuosi == 2020:
    print("ei ollut olympiavuosi, koska korona")
if vuosi == 1916:
    print("ei olympiavuosi, koska 1. maailmansota")
if vuosi == (1940 or 1944):
    print("ei olympiavuosi, koska 2. maailmansota")
else:
    print("ei ollut olympiavuosi")

#TAI

vuosi = int(input("Anna vuosiluku: "))
if vuosi % 4 == 0 or (vuosi != 2020 or vuosi != 1940 or vuosi != 1944):
    print("oli")
else:
    print("ei ollut")