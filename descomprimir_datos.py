import zipfile
import os

# Ruta del archivo .zip descargado
zip_file_path = 'C:/Users/Usuario/kaggle_downloads/house-prices-advanced-regression-techniques.zip'

# Ruta donde se comprime los archivos
extract_path = 'C:/Proyecto2-Entrega-1-Modelos-de-regresi-n-lineal'

if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Descomprimir el archivo
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Archivos extraídos a: {extract_path}")
