# ----------------------------------
# Ćw 2 b)
def parzysty_indeks(slowo):
    return slowo[2::2]


def ostatnie_znaki(slowo):
    return slowo[-n:]


def odwrotnosc(slowo):
    return slowo[::-1]


def palindrom(slowo):
    odwrotnosc_slowo = slowo[::-1]
    return slowo == odwrotnosc_slowo

def ktory_dluzszy(slowo, slowo2):
    if len(slowo) > len(slowo2):
        return slowo
    else:
        return slowo2

def format(imie, data_ur):
    str = 'My name is {}. My date of birth is {}.'
    return str.format(imie, data_ur)

# imie = input("Podaj swoje imie: ")
# data_ur = input("Podaj swoją date ur: ")
# slowo = input("Podaj slowo: ")
# slowo2 = input("Podaj slowo: ")

# print(parzysty_indeks(slowo))
# n = int(input("Podaj ilość ostatnich znaków: "))

# print(ostatnie_znaki(slowo))

# print(odwrotnosc(slowo))

# print(palindrom(slowo))

# print(ktory_dluzszy(slowo, slowo2))

# print(format(imie, data_ur))
