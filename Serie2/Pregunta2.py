# ---------------------------------------------------------------------------------
# 2. Análisis del precio en relación con diferentes características
# ---------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
sns.scatterplot(x="GrLivArea", y="SalePrice", data=train_df, ax=axes[0, 0])
axes[0, 0].set_title("Área habitable vs Precio de venta")

sns.boxplot(x="OverallQual", y="SalePrice", data=train_df, ax=axes[0, 1])
axes[0, 1].set_title("Calidad general vs Precio de venta")

sns.boxplot(x="GarageCars", y="SalePrice", data=train_df, ax=axes[1, 0])
axes[1, 0].set_title("Cantidad de autos en garaje vs Precio de venta")

sns.boxplot(x="KitchenQual", y="SalePrice", data=train_df, ax=axes[1, 1])
axes[1, 1].set_title("Calidad de la cocina vs Precio de venta")

plt.tight_layout()
plt.show()
