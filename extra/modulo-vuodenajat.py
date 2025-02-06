vuodenajat = ("Talvi","Kevät","Kesä","Syksy")
kuukausi = int(input("Anna kuukauden numero: "))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
  print(vuodenajat[0])
else:
  print(vuodenajat[(kuukausi - 1) // 3])

