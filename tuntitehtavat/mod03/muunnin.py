grammat = int(input("Kuinka monta grammaa: "))

kilot = (grammat) // 1000
vain_grammat = (grammat) % 1000

print(f"Määrä kiloina ja grammoina: {kilot} kg {vain_grammat} g")