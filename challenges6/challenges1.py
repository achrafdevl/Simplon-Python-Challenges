import pandas as pd
import numpy as np
data=[["Amine", 28, "Casablanca"],["Lina", 22, "Rabat"],["Youssef", 35, "Fès"],["Salma", 30, "Casablanca"],["Nora", np.nan, "Tanger"]]

# ! challenge 1

read = pd.DataFrame(data ,columns=["nom", "age", "ville"]) 
ds = read.head()
print(ds)

print("********************")

# infor = read.info()
# print(infor)

# print("********************")

# desc = read.describe()
# print(desc)

# print("********************")
# # ! challenge 2

# select = read["ville"]

# print(select)

# print("********************")

# agecon = read[read["age"] > 25]
# print(agecon)

# print("********************")

# nameAndVille = read[read["ville"] == "Casablanca"][["nom", "ville"]]
# print(nameAndVille)

# print("********************")

# # ! challenge 3

add = read["Année de Naissance"] = 2025 - read["age"]
print(add)

# print("********************")


# upper = read["nom"].str.upper()
# print(upper)

# print("********************")

# rename = read.rename(columns={"ville" : "Localisation" })
# print(rename)

# print("********************")


# ! challenge 4

# read.loc[4,"age"] = np.nan

# ds = read.head()
# print(ds)

# print("********************")


# null = read.isnull()
# print(null)


print("********************")

replace = read.fillna(read["age"].mean())
print(replace)


print("********************")


# ! challenge 5

# decroissant = read.sort_values(by='age', ascending=False)
# print(decroissant)


# print("********************")

# drop = read.drop("Année de Naissance", axis=1)
# print(drop)

# print("********************")


# dropLinge = read.drop(index=0)
# print(dropLinge)
