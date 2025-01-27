kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = (kanta + korkeus) * 2
pintaAla = kanta * korkeus

print(f"Piiri: {piiri: <10.3f}")
print(f"Pinta-ala: {pintaAla: <10.3f}")
print(f"Piiri: {piiri: 10.3f}")
print(f"Pinta-ala: {pintaAla: 10.3f}")