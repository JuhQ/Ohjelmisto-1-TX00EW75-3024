a = ['Juha','Hannu']
b = ['Muut','Innovaatioprojekti tyypit']

#print(b)

b.extend(a)
#print(b)
# lista ei voi olla remove() metodin parametrina
#b.remove(a)
#print(b)

# sisäkkäiset listat on ok
#                     0       1               2                   3
#                                      0      1       2
lista_listoista = [[1,2,3],[4,5,6],[['ja', 'niin', 'eespäin'],[]],[]]

print(lista_listoista)
print(lista_listoista[2])
print(lista_listoista[2][0])
print(lista_listoista[2][0][2])
print(lista_listoista[2][0][2][2:])
print(lista_listoista[2][0][0::2])
print(lista_listoista[2][0][1])

"""
for i in range(0, len(b)):
    print(i)
    arvo = b[i]
    print(arvo)
    #b.remove(arvo)

#for arvo in a:
#    print(arvo)

print(arvo)

print(b)
"""