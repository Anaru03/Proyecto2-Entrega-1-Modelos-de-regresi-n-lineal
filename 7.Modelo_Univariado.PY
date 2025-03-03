import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Cargar el conjunto de datos
readcsv = pd.read_csv("C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal/train.csv")

# Seleccionar la variable 'GrLivArea' y 'SalePrice' para el modelo univariado
X = readcsv[['GrLivArea']]  # Variable independiente
y = readcsv['SalePrice']  # Variable dependiente (precio de la casa)

# Agregar una constante para el modelo de regresión (intercepto)
X = sm.add_constant(X)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar el modelo de regresión lineal univariada
modelo = sm.OLS(y_train, X_train).fit()

# Resumen del modelo
print(modelo.summary())

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Gráfico de la relación entre 'GrLivArea' y 'SalePrice' con la línea de regresión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_test['GrLivArea'], y=y_test, label='Datos reales', color='blue')
plt.plot(X_test['GrLivArea'], y_pred, color='red', label='Línea de regresión')
plt.xlabel('Área sobre el nivel del suelo (GrLivArea)')
plt.ylabel('Precio de la casa (SalePrice)')
plt.title('Regresión Lineal Univariada: GrLivArea vs SalePrice')
plt.legend()
plt.show()

# Graficar residuos
residuos = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuos)
plt.hlines(0, xmin=min(y_pred), xmax=max(y_pred), colors='red', linestyles='dashed')
plt.xlabel('Predicción de precio (SalePrice)')
plt.ylabel('Residuos')
plt.title('Residuos del Modelo de Regresión Lineal Univariado')
plt.show()
