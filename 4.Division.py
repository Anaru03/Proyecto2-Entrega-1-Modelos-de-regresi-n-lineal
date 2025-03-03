import pandas as pd

# Cargar los datos
import pandas as pd
from sklearn.model_selection import train_test_split

try:
    readcsv = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")
    print("Archivo cargado con éxito!")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")


print(f"Primeras filas del DataFrame:\n{readcsv.head()}")
print(f"Dimensiones del DataFrame: {readcsv.shape}")

# División 80-20 sin estratificación
X = readcsv.drop('SalePrice', axis=1)  # Características
y = readcsv['SalePrice']  # Variable objetivo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
