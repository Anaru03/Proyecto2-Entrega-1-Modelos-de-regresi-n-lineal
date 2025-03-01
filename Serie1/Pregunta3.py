import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

# ---------------------------------------------------------------------------------
# 1. Distribuciones de Variables Numéricas
# ---------------------------------------------------------------------------------
numerical_df = df.select_dtypes(include=['number'])

correlations = numerical_df.corr()["SalePrice"].dropna().sort_values(ascending=False)

top_numerical_cols = correlations.index[1:6]  # Excluyendo 'SalePrice'

plt.figure(figsize=(15, 8))

for i, col in enumerate(top_numerical_cols):
    plt.subplot(2, 3, i+1)  
    plt.hist(df[col], bins=30, edgecolor="black")
    plt.title(f"Distribución de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")

plt.suptitle("Principales Distribuciones de Variables Numéricas", fontsize=16)
plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()


# ---------------------------------------------------------------------------------
# 2. Distribuciones de Variables Categóricas
# ---------------------------------------------------------------------------------
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols[:5]:  # Tomamos solo las primeras 5 categorías
    plt.figure(figsize=(8, 6))
    sns.countplot(y=df[col], order=df[col].value_counts().index, palette="coolwarm")
    plt.title(f"Distribución de {col}")
    plt.show()