# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen
# saakka, kunnes tämä syöttää tyhjän merkkijonon
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista
# luvuista viisi suurinta suuruusjärjestyksessä suurimmasta
# alkaen. Vihje: listan alkioiden lajittelujärjestyksen
# voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []
luku = (input("anna luku tai paina enter lopettamiseksi: "))
while luku != "":
    luvut.append(luku)
    luku = (input("anna luku tai paina enter lopettamiseksi: "))
intluvut = luvut
intluvut = [int(num) for num in luvut]
intluvut.sort()
print(f"suurimmat luvut: {intluvut[-1]}, {intluvut[-2]}, {intluvut[-3]}, {intluvut[-4]}, {intluvut[-5]}")