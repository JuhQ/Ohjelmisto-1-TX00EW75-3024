#leiviskä = float(input("Anna leiviskät: "))
#naula = float(input("Anna naulat: "))
#luoti = float(input("Anna luodit: "))

leiviskä = 3
naula = 9
luoti = 13.5

luoti_grammana = 13.3
naula_luotina = 32
leiviskä_naulana = 20

luodit_grammoina = luoti * luoti_grammana
naulat_grammoina = naula * naula_luotina * luoti_grammana
leiviskät_grammoina = leiviskä * leiviskä_naulana * naula_luotina * luoti_grammana

total = luodit_grammoina + naulat_grammoina + leiviskät_grammoina

kilot = int(total / 1000)
grammat = total - (kilot*1000)

print()
print("Massa nykymittojen mukaan:")
print(f"{kilot: <.0f} kilogrammaa ja {grammat: <.2f} grammaa.")
print()
print(f"{total//1000: <.0f} kilogrammaa ja {(total/1000): <.2f} grammaa.")
#print(str(kilot) + " kilogrammaa ja " + str(grammat) + " grammaa.")