# kolekcja

# lista - przechowuje rózne typ, zachowuje kolenosc przy dodawaniu elementów
lista = []
lista_pusta = list()
print(lista_pusta)  # []
print(type(lista_pusta))  # <class 'list'>

lista_pusta.append("Andrzej")
lista_pusta.append("Tomek")
lista_pusta.append("Zenek")
lista_pusta.append("Aga")
print(lista_pusta)  # ['Andrzej', 'Tomek', 'Zenek', 'Aga']

lista_pusta.sort()
print(lista_pusta)  # ['Aga', 'Andrzej', 'Tomek', 'Zenek']

lista_pusta.append(345)
print(lista_pusta)  # ['Aga', 'Andrzej', 'Tomek', 'Zenek', 345]

# lista_pusta.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
lista_pusta = ['Aga', 'Andrzej', 'Tomek', 'Zenek']
lista_pusta.sort(reverse=True)
print(lista_pusta)  # ['Zenek', 'Tomek', 'Andrzej', 'Aga']

# indeksowanie od 0
lista_pusta.insert(1, 'Magda')
print(lista_pusta)  # ['Zenek', 'Magda', 'Tomek', 'Andrzej', 'Aga']

print(lista_pusta[0])  # Zenek
# print(lista_pusta[23])  # IndexError: list index out of range
print(lista_pusta[4])  # Aga
print(len(lista_pusta))  # 5
print(lista_pusta[len(lista_pusta) - 1])  # Aga
print(lista_pusta[-1])  # Aga

# slicowanie
print(lista_pusta[0:2])  # ['Zenek', 'Magda']
print(lista_pusta[:2])  # ['Zenek', 'Magda']
print(lista_pusta[1:])  # z ostatnim wlłącznie, ['Magda', 'Tomek', 'Andrzej', 'Aga']
print(lista_pusta[1:-1])  # bez ostatniego, ['Magda', 'Tomek', 'Andrzej']

print(lista_pusta[0:4:2])  # [start:stop:krok], ['Zenek', 'Tomek']
print(lista_pusta[::-1])  # ['Aga', 'Andrzej', 'Tomek', 'Magda', 'Zenek']

print(lista_pusta[45:90])  # []- pusta lista

print(lista_pusta.pop(3))  # Andrzej
print(lista_pusta)  # ['Zenek', 'Magda', 'Tomek', 'Aga']
print(lista_pusta.pop())  # usnie ostatni

lista_pusta.remove("Magda")
print(lista_pusta)  # ['Zenek', 'Tomek']

# rozpakowanie sekwencji
osoby = ["Tomek", "Ewa", 'Adam']
print(osoby)  # ['Tomek', 'Ewa', 'Adam']
osoby.extend(lista_pusta)
print(osoby)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek']
nowa_lista = osoby + lista_pusta
print(nowa_lista)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek', 'Zenek', 'Tomek']

osoby.append(lista_pusta)
print(osoby)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek', ['Zenek', 'Tomek']]

nnn_lista = nowa_lista  # kopia referencji
lista_copy = nowa_lista.copy()
print(nnn_lista)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek', 'Zenek', 'Tomek']
print(nowa_lista)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek', 'Zenek', 'Tomek']
nowa_lista.clear()  # usunięcie wszystkich elementów listy
print(nnn_lista)  # []
print(nowa_lista)  # []
print(lista_copy)  # ['Tomek', 'Ewa', 'Adam', 'Zenek', 'Tomek', 'Zenek', 'Tomek']

# krotka (tuple) -
