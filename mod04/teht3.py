# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

suku = input("anna sukupuoli: N tai M ")
arvo = int(input("anna hemoglobiiniarvo g/l "))

if suku == "N" and (117 <= arvo <= 175):
        print("normaali arvo")
if suku == "N" and arvo > 175:
        print("korkea arvo")
if suku == "N" and arvo < 117:
        print("alhainen arvo")

if suku == "M" and (134 <= arvo <= 195):
    print("normaali arvo")
if suku == "M" and arvo > 195:
    print("korkea arvo")
if suku == "M" and arvo < 134:
    print("alhainen arvo")

