# FUNKCJA zip(): Służy do łączenia elementów z dwóch lub więcej list w pary.
# Tworzy krotki, gdzie każdy element pochodzi z odpowiadających sobie miejsc w listach.

# FUNKCJA ENUMERATE()- dzięki niej można przypisać numer (indeks) każdego elementu w liście.

# FUNKCJA SORTED()- służy do porządkowania listy i zwracania jej posortowanej wersji.

# MODUŁ math - Zawiera różne funkcje matematyczne takie jak np.: sqrt() – pierwiastek kwadratowy,  pi – stała matematyczna,
# sin(), cos() – funkcje trygonometryczne
# MODUŁ random - Pozwala generować losowe wartości, np. randint() zwraca losową liczbę z zakresu.
# MODUŁ time - Umożliwia dodawanie opóźnień w programie.

# WYJĄTKI- Występują, gdy wystąpi błąd w programie, uniemożliwiający jego dalsze wykonywanie.
# Gdy zauważymy wyjątek możemy go zidentyfikować,naprawić bądź zignorować.
#Wszystkie wyjątki mają określone nazwy i ułożone są w hierarchicznej strukturze co pozwala na ich kategoryzowanie.

# WYJĄTEK ValueError- Powstaje, gdy funkcja otrzymuje dane w niewłaściwym formacie lub wartości,
# które nie mogą być poprawnie przetworzone.

# WYJĄTEK ZeroDivisionError- Pojawia się przy próbie dzielenia przez zero.
# WYJĄTEK KeyError – występuje, gdy próbujemy uzyskać dostęp do klucza w słowniku, który nie istnieje.

#ArithmeticError- pozwala uniknąć błędów, które mogłyby zatrzymać program. Możesz obsłużyć kilka różnych błędów.

# OBSŁUGA WYJĄTKÓW (try-except):
# TRY: Blok, w którym mogą wystąpić błędy.
# EXCEPT: Blok, który obsługuje błąd, jeśli wystąpi.

# Link do dokumentacji:
# https://docs.python.org/3/library/functions.html#zip
# https://docs.python.org/3/library/exceptions.html
# github:https://github.com/Morciax/python-intro

# FUNKCJA zip()
lista1 = [1, 2, 3]
lista2 = ['Jeleń', 'Małpa', 'Koziołek']
zwierzęta = list(zip(lista1, lista2))
print(zwierzęta)

# FUNKCJA ENUMERATE()
list = ['a', 'b', 'c']
for index, value in enumerate(list):
    print(index, value)

#Można stworzyć listę, do której użytkownik doda elementy, a następnie użyć zip() do ich połączenia i enumerate()
#do przypisania indeksów.

# Tworzenie pustych list
lista1 = []
lista2 = []
print("Podawaj elementy list. Wpisz 'end', aby zakończyć dodawanie.")

while True:
    elementy1 = input("Podaj elementy do pierwszej listy: ")
    if elementy1.lower() == "end":
        break
    elementy2 = input("Podaj element do drugiej listy: ")
    if elementy2.lower() == "end":
        break

    lista1.append(elementy1)
    lista2.append(elementy2)

# Łączenie i numerowanie obu list
nowa_lista = list(zip(lista1, lista2))
print('\nPołączona lista')
print(nowa_lista)
ponumerowana_lista = list(enumerate(nowa_lista))
print("\nPonumerowana i połączona lista:")
print(ponumerowana_lista)

# FUNKCJA SORTED()
unsorted_list = [3, 1, 2, 4, 5, 6]
sorted_list = sorted(unsorted_list)
print('\nPosortowana lista:')
print(sorted_list)

#Moduł math (np. sqrt)
import math
#obliczmy pierwiastek kwadratowy z 16.
print(math.sqrt(16))

#Moduł random
import random
print(random.randint(1, 100))
#program wyświetla nam losową liczbę w zakresie od 1-100 włącznie

#wyjątek ZeroDivisionError, try-except
try:
    wynik = 1 / 0
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero!")
