import numpy as np
import pandas as pd




# Ćw 1
f = open('tekst1', 'r+')
s = f.read()
print(s)
print(type(s))


# Ćw 2
data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype=('|U16'))
print(data)


# Ćw 3
data1 = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
data2 = data1.stack()
data3 = data2.str.replace(',', '.').astype('float')
srednia = data3.mean()
minCena = data3.min()
maxCena = data3.max()
print(data3[data3 == minCena])
print(data3[data3 == maxCena])


# Ćw 4
import matplotlib as plt
df = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
df.fillna(0, inplace=True)
df.str.replace(",", ".").astype('float')
print(df)



