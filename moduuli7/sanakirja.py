
avain1 = "jepulis"
arvo1 = "hepulis"
numerot = {
    "Juha": 123,
    "Hannu": 234,
    avain1: arvo1,
    "huh": arvo1,
    arvo1: "hevonen"
}

print(numerot)

numerot['Robbie'] = 5

print(numerot)

numerot["Kissat"] = "Koiria"

print(numerot)

del numerot['Kissat']

print(numerot)

for avain in numerot:
    print(avain)
    print(numerot[avain])


if "Juha" in numerot:
    print("Juha löytyy")
else:
    print("Juha ei löydy")


numerot['Juha'] = 678
print(numerot)


#print(numerot[0])
#print(numerot[1])


avain = "juu"
arvo = "koira"

def get_avain():
    return "juu"

# funktiokutsun palautusarvo voi olla avaimena
numerot[get_avain()] = get_avain()
#numerot["juu"] = arvo
#numerot["juu"] = "koira"
print(numerot)


# sanakirja sanakirjan arvona

osoitteet = {
    "Juha": {
        "email": "juha.tauriainen@metropolia.fi",
        "puhelin": "112",
        "bitcoin": "mom send bitcoins"
    }
}

print(osoitteet)
print(osoitteet["Juha"])
if "Hannu" in osoitteet:
    print(osoitteet["Hannu"])
