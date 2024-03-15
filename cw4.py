# Ćwiczenie 1

names = ["michal", "nela", "ola", "przemek"]

names_duzalitera = [x.capitalize() for x in names]
print(names_duzalitera)


names_tylkol = [x for x in names if "l" in x]
print(names_tylkol)


zenskie = ([x.capitalize() for x in names if x[len(x)-1] == 'a'])
print(zenskie)


sumaryczna = [len(x) for x in names]
print(sumaryczna)

# Ćwiczenie 2

# slowo = input("Podaj ciąg liter i cyfr: ")
dict = {
    "1" : "jeden",
    "2" : "dwa",
    "3" : "trzy",
    "4" : "cztery",
    "5" : "pięć",
    "6" : "sześć",
    "7" : "siedem",
    "8" : "osiem",
    "9" : "dziewięć"
}

# for x in slowo:
#     if x in dict.keys():
#         print(dict.get(x), end = " ")


# Ćwiczenie 3

def iloczyn(*num):
    sum = 1
    for n in num:
        sum = sum * n
    print("Iloczyn liczb:", sum)


iloczyn(1, 2, 3, 4, 5)


def suma(*num):
    sum = 0
    count = 1
    for x in num:
        sum = sum+x ** count
        count = count + 1
    return sum


print(suma(1,2,3,4))


def mean(*num):
    count = 0
    suma = 0
    for x in num:
        suma = suma + x
        count = count + 1
    return suma/count


print(mean(2,2,2))


def gmean(*num):
    count = 0
    suma = 1
    for x in num:
        suma = suma * x
        count = count + 1
    return pow(suma, 1/count)


print(gmean(8,8,8))


def sumaryczna_dlugosc(*string):
    suma = 0
    for x in string:
        suma = suma + len(x)
    return suma


print(sumaryczna_dlugosc("python", "kajak"))


def najw_i_najm(*num):
    najm = num[0]
    najw = num[0]
    for x in num:
        if x < najm:
            najm = x
    for y in num:
        if y > najw:
            najw = y
    return (najm, najw)


print(najw_i_najm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def intro(**string):
    for key, value in string.items():
        print("{} to {}".format(key, value))


intro(Imie = "Wiktor", NrTel = 123456789)