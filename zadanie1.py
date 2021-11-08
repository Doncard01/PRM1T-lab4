import math

N = 10
lista = []

def sinus(x):
    wynik = 0
    for n in range(N+1):
        dzialanie = ((-1)**n/math.factorial(2*n+1))*x**(2*n+1)
        wynik += dzialanie
        lista.append(wynik)
    print(wynik)
x = float(input("Podaj x: "))


sinus(x)
print(lista)

