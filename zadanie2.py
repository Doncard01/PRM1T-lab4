
lista = [7, 7, 2, 5, 1, 1, 4, 3, 7, 3, 9]

#print(len(lista))

def nie_powt(lista):
    ile = 0
    powt = []

    for i in lista:
        if i not in powt:
            ile += 1
            powt.append(i)
        else:
            ile -= 1
            powt.remove(i)

    print(ile)
    print(powt)


#nie_powt(lista)

def indeks0(lista):
    element = lista[0]

    for i in range(len(lista)):
        if lista[i] == element:
            print(f"Indeks {i}")

#indeks0(lista)

lista2 = nie_powt(lista)
print(lista2)