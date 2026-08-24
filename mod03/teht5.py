# Kirjoita ohjelma, joka kysyy käyttäjältä massan
# keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
# sekä ilmoittaa tuloksen käyttäjälle.

#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.

leiviska = float(input("anna leiviskät: "))
naula = float(input("anna naulat: "))
luoti = float(input("anna luodit: "))

luoti_g = (luoti * 13.3)
naula_g = (luoti * 32 * 13.3)
leiviska_g = (naula * 20 * 32 * 13.3)
kilot = (luoti_g + naula_g + leiviska_g) // 1000
grammat = (luoti_g + naula_g + leiviska_g) % 1000

print(f"luodit nykymittojen mukaan: {luoti_g} g, naulat nykymittojen mukaan: {naula_g} g, leiviskät nykymittojen mukaan: {leiviska_g} g")
print(f"massa nykymittojen mukaan: {kilot} kg {grammat} g")