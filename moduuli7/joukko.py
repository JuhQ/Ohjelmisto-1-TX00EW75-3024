
#joukko = {}
joukko = set()

joukko.add("Toinen")
joukko.add("Toinen")
joukko.add("Toinen")
joukko.add("Toinen")
joukko.add("toinen")
joukko.add("Toinen2")
joukko.add("TOINEN")
joukko.add("TOINEN")

print(joukko)
joukko.add("Kolmas")
print(joukko)

print(type(joukko))

joukko2 = {"Kolmas", "neljäs", "viides"}

print(joukko.union(joukko2))
print(joukko.intersection(joukko2))
print("Kolmas" in joukko)
print("Ei löydy" in joukko)

# in -avainsanalla voidaan tarkistaa löytyykö alkio joukosta
#if "Admin" in joukko:
#    salli_admin_ominaisuudet()



print("-----")
for arvo in joukko:
    print(arvo)


joukko.sort()

