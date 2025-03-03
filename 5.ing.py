import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar los datos
try:
    readcsv = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")
    print("Archivo cargado con éxito!")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")

# Mostrar información inicial
print(f"Primeras filas del DataFrame:\n{readcsv.head()}")
print(f"Dimensiones del DataFrame: {readcsv.shape}")

# 1. Manejo de valores nulos
readcsv.fillna(readcsv.median(numeric_only=True), inplace=True)  # Para datos numéricos
readcsv.fillna("None", inplace=True)  # Para datos categóricos

# 2. Codificación de variables categóricas
readcsv = pd.get_dummies(readcsv, drop_first=True)

# 3. Escalado de variables numéricas
scaler = StandardScaler()
numerical_cols = readcsv.select_dtypes(include=['int64', 'float64']).columns
readcsv[numerical_cols] = scaler.fit_transform(readcsv[numerical_cols])

# 4. Creación de nuevas características
readcsv["TotalSF"] = readcsv["TotalBsmtSF"] + readcsv["1stFlrSF"] + readcsv["2ndFlrSF"]

# División en conjuntos de entrenamiento y prueba (80-20 sin estratificación)
X = readcsv.drop('SalePrice', axis=1)  # Características
y = readcsv['SalePrice']  # Variable objetivo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Confirmar tamaños
print(f"Tamaño del conjunto de entrenamiento: {X_train.shape}")
print(f"Tamaño del conjunto de prueba: {X_test.shape}")
