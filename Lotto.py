#Napisz program, który:
#zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
        #czy wprowadzony ciąg znaków jest poprawną liczbą,
        #czy użytkownik nie wpisał tej liczby już poprzednio,
        #czy liczba należy do zakresu 1-49,
        #po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
        #wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
#poinformuje gracza, ile liczb trafił.

import random

def lotek():
    lista = []
    try:
        a = int(input("Podaj pierwszą liczbę: "))
        if a in range (1, 50):
            lista.append(a)
        else:
            print("Podaj numer z zakresu od 1 do 49!")
        b = int(input("Podaj drugą liczbę: "))
        if b in range(1, 50) and b not in lista:
            lista.append(b)
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!")
        c = int(input("Podaj trzecią liczbę: "))
        if c in range(1, 50) and c not in lista:
            lista.append(c)
        else:
            print("Podaj numer z zakresu od 1 do 49, numery nie mogą się powtarzać!")
        d = int(input("Podaj czwartą liczbę: "))
        if d in range(1, 50) and d not in lista:
            lista.append(d)
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!")
        e = int(input("Podaj piątą liczbę: "))
        if e in range(1, 50) and e not in lista:
            lista.append(e)
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!")
        f = int(input("Podaj szóstą liczbę: "))
        if f in range(1, 50) and f not in lista:
            lista.append(f)
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!")
    except (TypeError, ValueError):
        print("To nie jest liczba")
    lista.sort()
    print(f"Wybrałeś następujące liczby: {lista}")
    if len(lista) < 6:
        print("Spróbuj ponownie - wprowadź 6 liczb w zakresie od 1 do 49, liczby nie mogą się powtarzać")
    return(lista)

def losowanie():
    losy = []
    for n in range (1,7):
        n = random.randint(1, 50)
        losy.append(n)
    losy.sort()
    print(f"Komputer wylosował: {losy}")
    return(losy)


def porownanie():
    a = lotek()
    b = losowanie()
    c = [i for i in a if i in b]
    hits = 0
    for i in c:
            hits += 1
    print(f"Udało Ci się trafić {hits} {'liczbę' if hits == 1 else 'liczb'}!")


print(porownanie())