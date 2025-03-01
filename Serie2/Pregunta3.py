# ---------------------------------------------------------------------------------
# 3. Análisis de diferencias en el precio según el vecindario
# ---------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

plt.figure(figsize=(16, 6))
sns.boxplot(x="Neighborhood", y="SalePrice", data=train_df)
plt.title("Precio de venta por vecindario")
plt.xticks(rotation=90)
plt.show()
