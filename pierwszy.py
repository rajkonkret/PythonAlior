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
