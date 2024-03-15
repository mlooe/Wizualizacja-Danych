import math

def podpunktA(n):
    if n > 0 and n < 100:
        for x in range(0,n+1):
            wynik = n * x
            print(f'{n} * {x} = {wynik}')
    else:
        print("n is too large")


# n = int(input("Podaj liczbę: "))
# print(podpunktA(n))

def podpunktB(a,b):
    return None

# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
# print(podpunktB(a,b))

def podpunktC(n):
    e1 = (1 + 1/n)**n
    wynik = 0
    for k in range(n+1):
        e2 = 1/math.factorial(k)
        wynik = wynik + e2
    return f'wynik e1 = {e1}, wynik e2 = {e2}'


n = int(input("Podaj liczbe: "))
podpunktA(n)
