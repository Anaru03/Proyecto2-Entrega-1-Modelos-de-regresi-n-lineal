# ---------------------------------------------------------------------------------
# 2. Análisis de correlaciones con el Precio de Venta
# ---------------------------------------------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

df_numeric = df.select_dtypes(include=['number'])

correlations = df_numeric.corr()["SalePrice"].dropna().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.heatmap(correlations.to_frame(), annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
plt.title("Correlaciones con el Precio de Venta")
plt.show()
