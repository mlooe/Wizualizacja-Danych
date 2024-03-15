list1=[1,2,3,4,5,6,7,8,9,10]
list2=[10,20,30,40,50,60,70,80,90,100]
print(list1 + list2)

list3 = []
for x in list1:
    for y in list2:
        if list1.index(x) == list2.index(y):
            list3.append(x+y)
print(list3)


list4 = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
list4.sort()
print(list4)

dict = {
    "styczeń" : 1,
    "luty" : 2,
    "marzec" : 3,
    "kwiecień" : 4,
    "maj" : 5,
    "czerwiec" : 6,
    "lipiec" : 7,
    "sierpień" : 8,
    "wrzesień" : 9,
    "październik" : 10,
    "listopad" : 11,
    "grudzień" : 12
}


def numer_miesiaca(list4):
    list5 = []
    for x in list4:
        if x in dict.keys():
            list5.append(dict.get(x))
    return list5


print(numer_miesiaca(list4))


def lista_nazwisk():
    list6 = ["Kowalski", "Galant", "Miszczyk", "Wiesiński", "Abramczyk", "Batazynski", "Cyrkiewicz", "Dynkiewicz"]
    lst = []
    litera = input("Podaj literę: ")
    for x in list6:
        if x[0] > litera.upper():
            lst.append(x)
    return lst

# print(lista_nazwisk())


def dlugosc_nazwiska():
    list6 = ["Galant", "Kowalski", "Miszczyk", "Wiesiński", "Abramczyk", "Batazynski", "Cyrkiewicz", "Dynkiewicz", "Siesin"]
    list6.remove("Galant")
    list6.remove("Siesin")
    return list6


# print(dlugosc_nazwiska())

def najw_do_najm():
    list7 = [6, 5, 4, 4, 54, 35, 54, 6, 4, 8, 10, 0, 23, 99]
    najmniejsza = list7[0]
    for smallest in list7:
        if smallest < najmniejsza:
            najmniejsza = smallest
