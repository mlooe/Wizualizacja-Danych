# Ćw 1 -------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# x = np.linspace(-4,4 ,100)
# y = np.sin(2 * x)
# y1 = 2*np.sin(x)
# y2 = np.sin(x)
# plt.plot(x, y2, 'blue', linestyle="-", label="sin x")
# plt.plot(x , y1, 'red', linestyle=":", label="2sin(x)")
# plt.plot(x , y, 'green', linestyle="--", label="sin(2x)")
# plt.legend(title='Wykres' )





# Ćw 2 -------------------------------------------

# x = np.linspace(-10, 10, 100)
# y = 1/(1 + x**(2))
# plt.plot(x, y, 'green', linestyle="-", label="1/1+x**2")
# plt.legend(title='Wykres' )
#
#
# x = np.linspace(0, 3, 100)
# e = 2.71828182846
# y1 = x**2
# y2 = e**x
# y3 = x**x
#
#
# p1 = plt.plot(x, y1, 'red', linestyle="-", label="x ** 2")
# p2 = plt.plot(x, y2, 'blue', linestyle=":", label="e ** 2")
# p3 = plt.plot(x, y3, 'green', linestyle="--", label="x ** x")
# plt.legend(title='Wykres')
#
# x = np.linspace(0, 4, 100)
# p1 = plt.plot(x, y1, 'red', linestyle="-", label="x ** 2")
# p2 = plt.plot(x, y2, 'blue', linestyle=":", label="e ** 2")
# p3 = plt.plot(x, y3, 'green', linestyle="--", label="x ** x")
# plt.legend(title='Wykres')
# plt.show()


# x = np.linspace(0, 4, 100)
# e = 2.71828182846
# y1 = x**2
# y2 = e**x
# y3 = x**x
#
# plt.subplot(3, 1, 1)
# p1 = plt.plot(x, y1, 'red', linestyle="-", label="x ** 2")
# plt.legend(title='Wykres1')
#
# plt.subplot(3, 1, 2)
# p2 = plt.plot(x, y2, 'blue', linestyle=":", label="e ** 2")
# plt.legend(title='Wykres2')
#
#
# plt.subplot(3, 1, 3)
# p3 = plt.plot(x, y3, 'green', linestyle="--", label="x ** x")
# plt.legend(title='Wykres3')
# plt.show()


# Ćw 3 -------------------------------------------

import seaborn as sns

# przykładowe

def sinplot(flip = 1):
    x = np.linspace( 0,14,100 )
    for i in range (1, 5) :
        plt.plot(x, np.sin(x + i *.5)*(7 - i) * flip)
sns.set_style ("whitegrid")
sns.set_palette("husl")
sinplot()
print(sns.axes_style())
plt.show()


x = np.linspace(-2, 2, 100)
y1, y2, y3 = x, x**2, x**3
sns.set_style ("whitegrid")
sns.set_palette("husl")

plt.plot(x, y1, 'blue', linestyle="-", label="x")
plt.plot(x, y2, 'red', linestyle="-", label="x**2")
plt.plot(x, y3, 'green', linestyle="-", label="x**3")

x = np.linspace(0, 2, 100)
y4, y5 = np.sqrt(x), np.cbrt(x)
plt.plot(x, y4, 'red', linestyle="-", label="sqrt(x)")
plt.plot(x, y5, 'purple', linestyle="-", label="cube_square(x)")


plt.show()

# Ćw 4 -------------------------------------------


glue = sns.load_dataset("glue")

sns.catplot(
    data=glue,
    kind='violin',
    x='Year',
    y='Score',
    palette=['orange', 'green'],
    hue='Encoder',
    col='Model',
    height=4,
    aspect=0.5
)

plt.show()
