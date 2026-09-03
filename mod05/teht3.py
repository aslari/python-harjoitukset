# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja
# siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista
# luvuista pienimmän ja suurimman.

luvut = []
luku = (input("anna luku: "))
while luku != "":
    luvut.append(luku)
    luku = (input("anna luku: "))
intluvut = luvut
intluvut = [int(num) for num in luvut]
intluvut.sort()
print(f"pienin luku: {intluvut[0]}, suuring luku: {intluvut[-1]}")