# import sys

# a = 56 #Typ INT
# print(a)
# print(type(a))
# b = 5.5 #Typ FLOAT
# print(b)
# print(type(b))
# zmienna_text = 'Oto tekst' #Typ STRING (STR)
# print(zmienna_text)
# print(type(zmienna_text))

# a = 6
# b = 3.12
# b = 3
#
# c = a + b  # Dodawanie
# print(c)
# d = a - b  # Odejmowanie
# print(d)
# e = 4
# e1 = a / e  # Dzielenie częściowe
# print(e1)
# f = b // a  # Dzielenie Całkowite
# print(f)
# f = a // b
# print(f)
# g = a ** 2  # Potęgowanie
# print(g)
# h = pow(a, 2)  # Potęgowanie. Alternatywa
# print(h)
#
# i = 6 ** (1/2)  # Pierwiastkowanie
# j = pow(6, 1/2)  # Pierwiastkowanie Alternatywa
# print(i)
# print(j)
#
# # Można tylko łączyć zmienne znakowe
# k = 'wizualizacja danych'
# l = ' grupa '
# m = 2
# print(k+l)  # Łączenie znaków
# print(k+l+str(m))  # Łączenie znaków z int'em

# print('liczba a jest rowna {:d}, liczba b jest rowna {:.2f}'
#      .format(a, b))  # Numer w stringu. Formatowanie. Podobnie jak w j. C

# a = input('Wprowadź liczbę: ')
# print(a + ' to wartosc liczby a')
# print(type(a))
# a = int(a)  # Zamiana str na INT by móc pomnożyć przez 5
# print(a*5)
# print(type(a))
#  Drugi sposób (Potrzeba importowac pakiet sys)
# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline()  # Wyswietli na nowej linii
# print(b + ' to wartosc liczby b')
# print(type(b))

# LISTA I SŁOWNIKI
# lista = [5, 6, 2.2, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# lista.append(67)  # Dodaj na sam koniec listy.
# print(lista)
# lista.insert(1, 3.12)  # Wstaw do listy (<numer indeksu>, <obiekt>)
# print(lista)
# lista.extend([21, 22, 23])  # Dodanie kilku elementów na sam koniec listy
# print(lista)
# lista.pop(2)  # Usuń element z listy poprzez numer indeksu
# print(lista)
# lista.remove([2, 3, 4])  # Usun element z listy po wartości
# # del lista[1]  # Usun element z listy. Wprowadzając niczego usunie całą listę!
# print(lista)
# lista.reverse()  # Odwróć element listy
# print(lista)
# lista2 = [-3, 44, 5, 29,3.12]
# print(lista2)
# lista2.sort()  # Sortuj elementy, tylko gdy są liczby
# print(lista2)

# SŁOWNIK
# slownik = {'klucz': 'wartosc', 1: 2, 'a': 5, 4: 'b'}
# print(slownik)
# print(slownik[4])  # Pokaż wartość wybranego klucza
# slownik[6] = 45  # Dodaj klucz i wartość do danego słownika
# print(slownik)
# slownik.pop(1)  # Usun klucz wraz z jego wartością
# print(slownik)
# print(slownik.keys())  # Pokaz klucze
# print(slownik.values())  # Pokaz wartosci
# del slownik[6] # Usun klucz. Alternatywa
# print(slownik)

# FUNKCJE WARUNKOWE I PĘTLE

a = 6
b = 7

if a > b:
    print("a jest wiekszy od b")
elif a < b:  # Else If
    print("a jest mniejszy od b")
else:
    print("a jest rowny b")
