ikä = int(input("Anna ikä: "))
if 15<=ikä<18:
    paino = float(input("Anna paino (kg): "))
if (ikä>=18 or ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua.")

"""
tehtavia_tehty = "1"


python = "kivaa"
if tehtavia_tehty == 1 and python == "kivaa":
    print("hello")
    print("toinen")

pituus = 175
ohjelmointi = "ei ole kivaa"
ohjelmointi_on_parasta = ohjelmointi == "kivaa"
print(python == "kivaa" and not ohjelmointi_on_parasta)
print(python == "kivaa" and ohjelmointi_on_parasta)
"""
"""
if tehtavia_tehty >= 6:
    print("ehto täyttyy")
else:
    print("ehto ei täyty")
"""


rahat = float(input("Anna rahamäärä: "))
if rahat<=2:
    print("Voit ostaa latten.")