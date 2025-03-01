# ---------------------------------------------------------------------------------
# 4. Análisis de construcción y calidad
# ---------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pdf_info = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")


plt.figure(figsize=(12, 6))
sns.scatterplot(x="YearBuilt", y="SalePrice", data=pdf_info)
plt.title("Año de construcción vs Precio de venta")
plt.xlabel("Año de construcción")
plt.ylabel("Precio de venta")
plt.show()
