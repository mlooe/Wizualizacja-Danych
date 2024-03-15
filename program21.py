# ----------------------------------
# Ćw 1 a)
import math

a = 5.2

sufit = math.ceil(a)
podloga = math.floor(a)

# print(sufit)
# print(podloga)
# print(round(a))

def sprawdz_czy_int(x,y):
    if x.is_integer() and y.is_integer() == True:
        return x % y
    elif x.is_integer() or y.is_integer() == False:
        return {math.fmod(x, y)}


# x = float(input("Podaj liczbę x: "))
# y = float(input("Podaj liczbę y: "))
# print(sprawdz_czy_int(x,y))

def logarytm(a, n):
    wynik = 0
    for k in range(2, n+1):
        wynik = math.log(k, a)
        print(f'log{k, a} = {wynik}', end = ' | ')


# a = int(input("Podaj liczbę a: "))
# n = int(input("Podaj ilosc n: "))

# logarytm(a, n)

def matematyka(a):
    return math.exp(a), math.e**a, math.pow(math.e, a)


a = int(input("Podaj liczbę a: "))
print(matematyka(a))

# ----------------------------------
# Ćw 1 b)

print(math.pow(1, 0), 1**0)
print(math.remainder(6,4), 6%4)

print(math.cosh(1))
print(math.sinh(0))

# ----------------------------------




