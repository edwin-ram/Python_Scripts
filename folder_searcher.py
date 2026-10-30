#Script para buscar archivos de una carpeta (path-origen) copiarlos y pegarlos en otra (path-destino)

from pathlib import Path
import shutil

directorio_destino = Path("insertar/path/destino")
directorio_origen = Path("insertar/path/origen")

with open ("RUTAS_NOV_2026.txt") as archivo:
    for linea in archivo:
        nombre_item = linea.strip() #el metodo .strip() srive para limpiar cada linea de espacios en blanco, saltos de linea o tabuladores, solo deja el texto neto. 
        item_a_copiar = directorio_origen / nombre_item

        if item_a_copiar.exists():
            print(f"Encontrado {nombre_item}. Copiando...")
            try:
                if item_a_copiar.is_file():
                    shutil.copy(str(item_a_copiar), str(directorio_destino / nombre_item))
                elif item_a_copiar.is_dir():
                    shutil.copytree(str(item_a_copiar), str(directorio_destino / nombre_item))
                print(f"COPIA EXITOSA")
            except Exception as e:
                print(f"Error al copiar {nombre_item}: {e}")
        else:
            print(f"El archivo {nombre_item} no existe en la carpeta de origen")