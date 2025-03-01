import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

missing_values = df.isnull().sum()

missing_values = missing_values[missing_values > 0]

plt.figure(figsize=(12, 6))
sns.barplot(x=missing_values.index, y=missing_values.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.ylabel("Cantidad de valores faltantes")
plt.title("Valores faltantes por variable")
plt.show()
