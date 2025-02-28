import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Inicia sesión con la API de Kaggle
api = KaggleApi()
api.authenticate()

# Nombre de la competencia y el archivo a descargar
competition_name = 'house-prices-advanced-regression-techniques'

# Ruta donde se descargará el archivo
download_path = 'C:/Users/Usuario/kaggle_downloads'

# Verifica si la ruta existe, si no la crea
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Descargar los archivos del conjunto de datos
print(f"Descargando archivos de la competencia: {competition_name}...")
api.competition_download_files(competition_name, path=download_path)

print("¡Descarga completada!")
