# Napisac program który po wprowadzeniu danej liczby daje wynik 0 po odejmowaniu cyfry z tabeli. tabela zawiera tylko
# liczby całkowite.
lista = [1, 3, 2, 4, 5]
licznik = 0
print('Prosze wprowadzic dana liczbe:')
a = int(input())
int(a)

while licznik<len(lista):
    if (a-lista[licznik])==0:
        print("Podana liczba jest z listy")
        break
    licznik +=1
else:
    print("Podana liczba nie jest z listy")