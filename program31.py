lista = []
for x in range(15):
    lista.append(x)
print(lista)


lista2 = []
for x in lista:
    lista2.append(x**5)
print(lista2)


lista3 = []
for x in range(1,21):
    lista3.append(x)
print(lista3)


lista4 = []
i = 1
for x in lista3:
    i = i * x
    lista4.append(i)
print(lista4)


lista5 = []
e = 2.178
for x in lista3:
    lista5.append(e**x)
print(lista5)


lista6 = []
lista6.append("Kowalski")
lista6.append("Galant")
lista6.append("Miszczyk")
lista6.append("Wiesiński")

lista7 = []
for x in lista6:
    lista7.append(len(x))
print(lista7)

