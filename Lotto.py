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
        a = int(input("Podaj pierwszą liczbę: ")) #poproś o wpisanie liczby
        if a in range (1, 50):
            lista.append(a)
        else:
            print("Podaj numer z zakresu od 1 do 49!") #jeśli liczba w przedziale 1-50, dodaj do listy lista, jeśli nie - zwróć odpowiedź
        b = int(input("Podaj drugą liczbę: "))
        if b in range(1, 50) and b not in lista:
            lista.append(b) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        c = int(input("Podaj trzecią liczbę: "))
        if c in range(1, 50) and c not in lista:
            lista.append(c) # jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Podaj numer z zakresu od 1 do 49, numery nie mogą się powtarzać!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        d = int(input("Podaj czwartą liczbę: "))
        if d in range(1, 50) and d not in lista:
            lista.append(d) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        e = int(input("Podaj piątą liczbę: "))
        if e in range(1, 50) and e not in lista:
            lista.append(e) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        f = int(input("Podaj szóstą liczbę: "))
        if f in range(1, 50) and f not in lista:
            lista.append(f) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Podaj numer z zakresu od 1 do 49, liczby nie mogą się powtarzać!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
    except (TypeError, ValueError):
        print("To nie jest liczba") #jeśli liczba nie spełni żadnych powyższych warunków, wyświetl odpowiedż
    lista.sort()
    print(f"Wybrałeś następujące liczby: {lista}") #wyświetl wszystkie wybrane przez gracza liczby
    if len(lista) < 6: #jeśli gracz nie wprowadzi 6 liczb spełniajacych powyższe warunki, wyświetl informację
        print("Spróbuj ponownie - wprowadź 6 liczb w zakresie od 1 do 49, liczby nie mogą się powtarzać")
    return(lista)

def losowanie():
    losy = []
    for n in range (1,7): #losowanie komputera - sześciokrotne wybranie losowej liczby z zakresu od 1 do 50
        n = random.randint(1, 50)
        losy.append(n)
    losy.sort()
    print(f"Komputer wylosował: {losy}")
    return(losy) #funkcja zwraca listę wybranych przez komputer liczb


def porownanie(): #funkcja porównująca wylosowane przez gracza i przez komputer liczby
    a = lotek()
    b = losowanie()
    c = [i for i in a if i in b]
    hits = 0
    for i in c: #funkcja licząca, ile liczb powtarza się w obu listach - gracza i komputera
            hits += 1
    print(f"Udało Ci się trafić {hits} {'liczbę' if hits == 1 else 'liczb'}!")


print(porownanie())