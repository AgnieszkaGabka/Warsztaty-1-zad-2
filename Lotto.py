#Program, który:
#zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
        #czy wprowadzony ciąg znaków jest poprawną liczbą,
        #czy użytkownik nie wpisał tej liczby już poprzednio,
        #czy liczba należy do zakresu 1-49,
        #po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
        #wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
#poinformuje gracza, ile liczb trafił.

import random

def lotto():
    list = []
    try:
        a = int(input("Enter the first number: ")) #poproś o wpisanie liczby
        if a in range (1, 50):
            list.append(a)
        else:
            print("Enter a number between 1 and 49!") #jeśli liczba w przedziale 1-50, dodaj do listy lista, jeśli nie - zwróć odpowiedź
        b = int(input("Enter the second number: "))
        if b in range(1, 50) and b not in list:
            list.append(b) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Enter a number from 1 to 49, numbers cannot be repeated!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        c = int(input("Enter the third number: "))
        if c in range(1, 50) and c not in list:
            list.append(c) # jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Enter a number from 1 to 49, numbers cannot be repeated!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        d = int(input("Enter the fourth number: "))
        if d in range(1, 50) and d not in list:
            list.append(d) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Enter a number from 1 to 49, numbers cannot be repeated!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        e = int(input("Enter the fifth number: "))
        if e in range(1, 50) and e not in list:
            list.append(e) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Enter a number from 1 to 49, numbers cannot be repeated!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
        f = int(input("Enter the sixth number: "))
        if f in range(1, 50) and f not in list:
            list.append(f) #jeśli gracz nie wybierał wcześniej takiej liczby, dodaj ją do listy
        else:
            print("Enter a number from 1 to 49, numbers cannot be repeated!") #jeśli dane nie spełnią powyższych warunków, wyświetl odpowiedż
    except (TypeError, ValueError):
        print("This is not a number") #jeśli liczba nie spełni żadnych powyższych warunków, wyświetl odpowiedż
    list.sort()
    print(f"You chose the following numbers: {list}") #wyświetl wszystkie wybrane przez gracza liczby
    if len(lista) < 6: #jeśli gracz nie wprowadzi 6 liczb spełniajacych powyższe warunki, wyświetl informację
        print("Try again - enter 6 numbers between 1 and 49, numbers cannot be repeated")
    return(list)

def lottery():
    lots = []
    for n in range (1,7): #losowanie komputera - sześciokrotne wybranie losowej liczby z zakresu od 1 do 50
        n = random.randint(1, 50)
        lots.append(n)
    lots.sort()
    print(f"Computer drew: {lots}")
    return(lots) #funkcja zwraca listę wybranych przez komputer liczb


def comparison(): #funkcja porównująca wylosowane przez gracza i przez komputer liczby
    a = lottery()
    b = losowanie()
    c = [i for i in a if i in b]
    hits = 0
    for i in c: #funkcja licząca, ile liczb powtarza się w obu listach - gracza i komputera
            hits += 1
    print(f"You hit {hits}!")


print(comparison())