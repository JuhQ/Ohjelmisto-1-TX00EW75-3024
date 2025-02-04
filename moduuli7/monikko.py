
python_opettajat = ('Juha', 'Hannu')

print(python_opettajat)
print(python_opettajat[0])
print(python_opettajat[1])
print(python_opettajat[-1])
print(python_opettajat[-2])
print(len(python_opettajat))

for ope in python_opettajat:
    print(ope)

#python_opettajat[0] = 'Hello'

def monikon_palauttava_funktio():
    #tuple = ("Monikko","on","englanniksi","tuple")
    return "Monikko", "tuple"

print(monikon_palauttava_funktio())


hedelmät = ("Appelsiini", "Mansikka", "Banaani", "Omena")
# alla oleva monikon purku muuttujiin ei toimi, sillä muuttujia on viisi, kun taas monikossa on neljä arvoa
(eka, toka, kolmas, neljäs, viides) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")

