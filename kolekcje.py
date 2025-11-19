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

# krotka (tuple) - niemutowalna lista
# pozwala lepiej zarządzać pamięcią
krotka = (23, 34, 54, "Radek")
print(krotka)
print(type(krotka))  # <class 'tuple'>

krotka2 = "Radek"
krotka3 = "Radek",
krotka4 = ("Radek")
krotka5 = ("Radek",)  # zalecenie pep8
print(type(krotka3), type(krotka4), type(krotka5), type(krotka2))
# <class 'tuple'> <class 'str'> <class 'tuple'> <class 'str'>

print(len(krotka))  # 4
# krotka[5] = 7# TypeError: 'tuple' object does not support item assignment

# rozpakowanie krotki
a, b, c, d = krotka
print(a, b, c, d)  # 23 34 54 Radek

a, b, *c = krotka  # * - worek na dane
print(a, b, c)  # 23 34 [54, 'Radek']

# słownik
# dane typu klucz-wartosc
oceny = {
    "Tomek": 4,
    "Radek": 5,
    "Agata": 5,
    "Jacek": 4,
}
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 5, 'Jacek': 4}
print(type(oceny))  # <class 'dict'>
# null -> None
print(oceny["Tomek"])  # 4
# print(oceny["tomek"])  # KeyError: 'tomek'
print(oceny.get("tomek"))  # None
print(oceny.get("Tomek"))  # 4
print(oceny.get("tomek", "Default"))  # Default

print(oceny.keys())
print(oceny.values())
print(oceny.items())
# dict_keys(['Tomek', 'Radek', 'Agata', 'Jacek'])
# dict_values([4, 5, 5, 4])
# dict_items([('Tomek', 4), ('Radek', 5), ('Agata', 5), ('Jacek', 4)])

oceny["Agata"] = 6
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 6, 'Jacek': 4}
oceny["Tomek"] = lista_pusta
print(oceny)
# {'Tomek': ['Zenek', 'Tomek'], 'Radek': 5, 'Agata': 6, 'Jacek': 4}
print(oceny['Tomek'])  # ['Zenek', 'Tomek']
print(oceny['Tomek'][0])  # Zenek

dictionary = {}
dict_pusty = dict()
print(dictionary)  # {}
print(dict_pusty)  # {}
print(dictionary)
print(type(dictionary))  # <class 'dict'>

# set() - zbiór
# przechowuja unikalne watości
# nie posiadaja indeksy
zbior1 = {45, 55, 66, 77}
zbior2 = {45, 55, 166, 177}

zbior1.add(101)
zbior1.add(102)
zbior1.add(105)
zbior1.add(77)
zbior1.add(55)
print(zbior1)  # {66, 101, 102, 105, 45, 77, 55}

# czesc wspolna
print(zbior1.intersection(zbior2))  # {45, 55}

print(zbior1 - zbior2)  # {66, 101, 102, 105, 77}
print(zbior1.difference(zbior2))  # {66, 101, 102, 105, 77}

pusty_zbior = set()
print(pusty_zbior)  # set()
print(type(pusty_zbior))  # <class 'set'>

lista_ze_zbioru = list(zbior1)
print(lista_ze_zbioru)  # [66, 101, 102, 105, 45, 77, 55]
lista = [66, 101, 102, 105, 45, 77, 55, 66, 77, 55]
zbior_z_listy = set(lista)
# tracimy kolejnosc
print(zbior_z_listy)  # {66, 101, 102, 105, 45, 77, 55}
