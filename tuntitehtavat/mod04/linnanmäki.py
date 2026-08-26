# lasten laitteisiin saa mennä yli 100cm
# kaikkiin laitteisiin saa mennä yli 140cm
# kirnuun alle 195cm

pituus = float(input("kuinka pitkä olet? "))
ika = int(input("kuinka vanha olet? "))

if pituus < 100:
    print("ei pääse mihinkään laitteeseen")
elif 100 <= pituus < 140:
    print("saa mennä lasten laitteisiin")
elif pituus >= 140:
    print("saa mennä kaikkiin laitteisiin")
elif 140 >= pituus <= 195:
    print("saa mennä kaikkiin laitteisiin ja kirnuun")
elif ika >= 8 and pituus >= 140:
    print("saa mennä kaikkiin laitteisiin ja tulirekeen")

else:
    print("ei pääse mihinkään laitteeseen.")


#TAI

pituus = float(input("kuinka pitkä olet? "))

if pituus >= 140:
    ika = int(input("kuinka vanha olet? "))
    if ika >= 8:
        print("pääset kaikkiin")
    else:
         print("pääset kaikkiin paitsi tulirekeen")