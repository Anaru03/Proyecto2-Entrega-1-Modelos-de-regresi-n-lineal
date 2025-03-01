# ---------------------------------------------------------------------------------
# 1. Análisis de precios según el tipo de vivienda
# ---------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

plt.figure(figsize=(12, 6))
sns.boxplot(x="BldgType", y="SalePrice", data=train_df)
plt.title("Distribución de precios por tipo de vivienda")
plt.xticks(rotation=45)
plt.show()
