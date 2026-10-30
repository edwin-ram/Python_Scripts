#Scritp para descompirmir archivos .gzip

import gzip
import shutil
import pandas as pd

# Definir los nombres de los archivos
archivo_comprimido = 'archivo.csv.gzip'
archivo_descomprimido = 'tu_archivo.csv'

# Abrir el archivo comprimido y copiar su contenido al nuevo archivo CSV
with gzip.open(archivo_comprimido, 'rb') as f_entrada:
    with open(archivo_descomprimido, 'wb') as f_salida:
        shutil.copyfileobj(f_entrada, f_salida)

print(f"¡Archivo descomprimido con éxito en: {archivo_descomprimido}!")

df = pd.read_csv(archivo_descomprimido)
print(df)