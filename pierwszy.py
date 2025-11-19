# https://peps.python.org/pep-0008/
# snake_case
import sys

print()
# ctrl alt l - formatowanie wg pep8
# ctrl d - powielanie lini
print("Nazywam się Radek")  # wypisz/wydrukuj
print('Radek')
# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\radek\PycharmProjects\PythonAlior\pierwszy.py", line 9
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)

# type() - sprawdzenie typu danych
print(type('Radek'))  # <class 'str'>

print("39" + "14")  # konkatenacja, łacenie tekstów, 3914

print(39 + 14)  # 53
# print("39" + 14)  # TypeError: can only concatenate str (not "int") to str

# silne typowanie
print(39 + 14)
print(type(39))  # <class 'int'>, całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

# zmienna - pudełko na dane
# typowanie dynamiczne
name = "Radek"
print(name)
print(type(name))
# Radek
# <class 'str'>
name = 90
print(type(name))
print(name)
# <class 'int'>
# 90

# podpowiedzi
name: str = 90
print(name)

# mypy
# pip install mypy
# mypy .\pierwszy.py

tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))

# tesksty sa niemutowalne
""" Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
zmienna = tekst.upper()
print("Zmienna:", zmienna)  # Zmienna: WITAJ ŚWIECIE

print(tekst.lower())
print(tekst.capitalize())  # Witaj świecie

zmienna1 = "GROSS"
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # == porównaniwe, False
print(zmienna1.casefold() == zmienna2.casefold())  # True

print(1 != 8)  # != różne
# rzutowanie - zamiana typu
print(int("39"))  # zamiana na int
print(str(39))
# 39
# 39

# typ logiczny
# True, False

print(int(True))  # 1
print(int(False))  # 0

# boolean
print(bool(100))
print(bool("Radek"))  # True

print(bool(""))  # False

# None - odpowiednik null, stan nieokreślony, nie wiem

temp = 36.6
print(type(temp))  # <class 'float'>, zmiennoprzecinowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024,
# max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal

# f - string format
print(f"Nazywa się {name}")  # Nazywa się 90
print("NAzywam się {}".format(name))  # NAzywam się 90

liczba = 3.90001
print(f"Wersja pythona: {liczba}")  # Wersja pythona: 3.90001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90
print(f"Wersja pythona: {liczba:.0f}")  # zaokragla Wersja pythona: 4

print(f"""
Tekst
    wielolinijkowy
""")
# Tekst
#     wielolinijkowy

"""komentarz 
    wielolinjkowe
    dokumentacja"""
print()
print(print.__doc__)

starszy = "Mam na imię %s"  # %s - str
print(starszy % name)  # Mam na imię 90
# print("Mam %i lat" % "Radek") # TypeError: %i format: a real number is required, not str

print("Wynik:", liczba)  # Wynik: 3.90001
# sep
#         string inserted between values, default a space.
# sep=" ", end="\n"
print("Wynk:", liczba, sep="....")  # Wynk:....3.90001

print(100 / 3)
print(100 // 3)  # częśc całkowita z dzielenia
print(100 % 3)  # modulo, reszta z dzielenia, 1

zysk = 456789123456
print(f"NAsza duza liczba: {zysk}")
print(f"NAsza duza liczba: {zysk:,}")  # NAsza duza liczba: 456,789,123,456
print(f"NAsza duza liczba: {zysk:_}")  # NAsza duza liczba: 456_789_123_456
print(f"NAsza duza liczba: {zysk:_}".replace("_", " "))
# NAsza duza liczba: 456_789_123_456
# NAsza duza liczba: 456 789 123 456
print(f"NAsza duza liczba: {zysk:_}".replace("_", "."))
# NAsza duza liczba: 456.789.123.456

parametr = 100_000_000_000
print(parametr)  # 100000000000
print(type(parametr))  # <class 'int'>

encoded_text = tekst.encode("utf-8")
print(encoded_text)  # b'Witaj \xc5\x9awiecie' - dane bajtowe
# \xc5\x9a - w kodzie szesnastkowym
print(encoded_text.decode('utf-8'))  # Witaj Świecie
