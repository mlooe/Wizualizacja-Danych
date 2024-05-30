import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a)
p = pd.read_csv('penguins.csv',
                header=0,
                usecols=["species", "body_mass_g", "sex"]
                )

p = p.dropna()
p = p.groupby(["sex", "species"])["body_mass_g"].mean()
print(p.to_string())


# b)
p = pd.read_csv('penguins.csv',
                header=0
                )

p = p.dropna()

min_value = p["body_mass_g"].min()
max_value = p["body_mass_g"].max()


# c)
p = pd.read_csv('penguins.csv',
                header=0,
                )

p = p.dropna()

print(p.value_counts(["species", "island"]))


# d)
p = pd.read_csv('penguins.csv',
                header=0,
                )

p = p.dropna()

print(p.value_counts(["species", "island"])["Adelie"])


# e)



