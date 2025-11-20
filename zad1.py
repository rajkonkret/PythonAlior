# pip install numpy

import numpy as np

lista = [2, 4, 6, 8, 10]

a = np.array(lista)
print(a)
print(type(a))
# [ 2  4  6  8 10]
# <class 'numpy.ndarray'>
print(a.dtype)  # int64

print(a.shape)  # (5,)

p = np.zeros((3, 3))
print(p)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
print(p.dtype)  # float64

q = np.ones((2, 2))
print(q)
print(q.dtype)
# [[1. 1.]
#  [1. 1.]]
# float64
r = np.full((2, 2), 4)
print(r)
print(r.dtype)
# [[4 4]
#  [4 4]]
# int64

s = np.eye(4)
print(s)
print(s.dtype)  # float64
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

t = np.random.random((3, 3))
print(t)
print(t.dtype)
# [[0.03913363 0.91363916 0.97260314]
#  [0.98048299 0.02525246 0.77466408]
#  [0.88922161 0.43146563 0.38707038]]
# float64

t1 = np.random.randint(0, 3, 3)
print(t1)  # [1 2 1]

lista2 = [[5, 6], [7, 8]]
b = np.array(lista2)
print(b)
# [[5 6]
#  [7 8]]

# ravel() - spłaszczanie, zwraca nowy obiekt
print(b.ravel())  # [5 6 7 8]

print(b[0])  # [5 6]

print(np.float64(21))  # 21.0
print(np.int64(22.0))  # 22

print(np.bool(21))  # True

print(np.float64(True))  # 1.0

arr = np.arange(1, 11, dtype=np.float64)
print(arr)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

# reshape - zmiana kształtu
arr = np.arange(12)
print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

new_arr = arr.reshape(4, 3)
print(new_arr)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

new_arr = arr.reshape(3, 4)
print(new_arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# new_arr = arr.reshape(3, 5)
# print(new_arr)
# ValueError: cannot reshape array of size 12 into shape (3,5)

# ravel() - zwraca widok
print(new_arr.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# flatten() - zwraca kopię
print(new_arr.flatten())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

flat = new_arr.flatten()  # kopia
rav = new_arr.ravel()  # widok, wplywa na oryginał

flat[0] = 999
rav[1] = 888

print(new_arr)
# [[  0 888   2   3]
#  [  4   5   6   7]
#  [  8   9  10  11]]

# transpose() - zamienia osie
print(new_arr.transpose())
# [[  0   4   8]
#  [888   5   9]
#  [  2   6  10]
#  [  3   7  11]]

# resize() - zmienia kształi  rozmiar tablicy, brakujące wypełni zerami, in-place - zmienia oryginał
new_arr.resize(1, 12)
print(new_arr)
# [[  0 888   2   3   4   5   6   7   8   9  10  11]]

arr1 = np.arange(1, 10).reshape(3, 3)
print(arr1)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(np.__version__)  # 2.3.5

# brodcasting - wykonanie operacji na wszystkich elementach tablicy
arr2 = 2 * arr1
print(arr2)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

lista_p = [1, 2, 3]
print(lista_p * 2)  # [1, 2, 3, 1, 2, 3]
print(list(range(100)))
arrx = arr1 + arr2
print(arrx)
#  [[ 3  6  9]
#  [12 15 18]
#  [21 24 27]]

# hstack() # skleił jako kolumny
arr3 = np.hstack((arr1, arr2))
print(arr3)
# [[ 1  2  3  2  4  6]
#  [ 4  5  6  8 10 12]
#  [ 7  8  9 14 16 18]]

# vstack()
arr4 = np.vstack((arr1, arr2))
print(arr4)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

# concatenate()
arr6 = np.concatenate((arr1, arr2), axis=0)
print(arr6)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]
arr7 = np.concatenate((arr1, arr2), axis=1)
print(arr7)
# [[ 1  2  3  2  4  6]
#  [ 4  5  6  8 10 12]
#  [ 7  8  9 14 16 18]]

arre1 = np.array([1, 2, 3])
arre2 = np.array([4, 5, 6])
np.concatenate((arre1, arre2), axis=0)
# numpy.exceptions.AxisError: axis 1 is out of bounds for array of dimension 1
# np.concatenate((arre1, arre2), axis=1)
# [[ 1  2  3  2  4  6]
#  [ 4  5  6  8 10 12]
#  [ 7  8  9 14 16 18]]

arr7 = np.dstack((arr1, arr2))
print(arr7)
# [[[ 1  2]
#   [ 2  4]
#   [ 3  6]]
#
#  [[ 4  8]
#   [ 5 10]
#   [ 6 12]]
#
#  [[ 7 14]
#   [ 8 16]
#   [ 9 18]]]

arr8 = np.arange(4, 7)
arr9 = 2 * arr8
arr_col_stack = np.column_stack((arr8, arr9))
print(arr_col_stack)
# [[[ 1  2]
#  [ 2  4]
#  [ 3  6]]
#
# [[ 4  8]
#  [ 5 10]
#  [ 6 12]]
#
# [[ 7 14]
#  [ 8 16]
#  [ 9 18]]]

arr_row_stack = np.row_stack((arr8, arr9))
print(arr_row_stack)
# C:\Users\radek\PycharmProjects\PythonAlior\zad1.py:218:
# DeprecationWarning: `row_stack` alias is deprecated. Use `np.vstack` directly.
#   arr_row_stack = np.row_stack((arr8, arr9))
# [[ 4  5  6]
#  [ 8 10 12]]
