import numpy as np
import pandas as pd

# Ćw 1
# a)

my_series = pd.Series([1, 2, 3, 4], ["a", "b", "c", "d"])
print(my_series["d"])


my_frame = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]])


lista = [1, 2, 3, 4, 5]
liczby = [x for x in lista]
new_series = pd.Series(liczby)


lista2 = [x for x in new_series]
print(lista2)


arr = np.array([6, 7, 5, 4])
liczby = [x for x in arr]
new_series = pd.Series(liczby)


liczby = [x for x in new_series]
new_frame = np.array(liczby)


s1 = pd.Series([2, 6, 5, 4])
s2 = pd.Series([1, 2, 3, 4])

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)

import random

lista = []
for x in range(0, 10):
    lista.append(random.randrange(-10, 10))

s3 = pd.Series(lista)
print(s3)

lista2 = []
for x in s3:
    if x < 0:
        lista2.append(x)

s4 = pd.Series([lista2])
print(s4)


# b)

my_list = [1, 32, -37, 91, 12, 11, -5]

my_dict = {'a' : [1, 3, 2], 'b' : [2, 5, 7], 'c' : [3, 4, 8], 'd' : [4, 10, 12]}

my_array = np.array([[1, 2, 5],[-2, 3, 3], [5, 2, 6]])

my_series = pd.Series ([1, 32, -37, 91, 12, 11, -5], index = ['a','b','c','d','e','f','g'])


df = pd.DataFrame(my_list)
df2 = pd.DataFrame(my_dict)
df3 = pd.DataFrame(my_array)
df4 = pd.DataFrame(my_series)

#nie dokończone


# c)
df5 = pd.DataFrame(
    [[1, 2, 4, 5],
     [-3, 8, 0.5, 10],
     [2, -5, 7, 3]],
    index=["l1", "l2", "l3"],
    columns=['b', 'c', 'd', '']
)

print(df5)
print(df5.reset_index())
print(df5.drop(columns=['', 'd']))
print(df5.sort_values('b'))




