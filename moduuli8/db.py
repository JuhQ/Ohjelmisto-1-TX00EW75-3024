import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True,
    #collation='utf8mb3_general_ci',
    collation='utf8mb3_unicode_ci'
)

ICAO = "AD-0002"

sql = f"SELECT name, iso_country, mun FROM airport WHERE ident = '{ICAO}'"
sql = f"SELECT * FROM airport LIMIT 10"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(sql)
print(tulos)
print(tulos[1:3])
print(tulos[0][1])

name = tulos[0]
municipality = tulos[1]

(name, municipality) = tulos

print(f"Name: {name}")

for monikko in tulos:
    #print("for in loopin sisällä")
    print(monikko)
    for alkio in monikko:
        print(f"  {alkio}")





