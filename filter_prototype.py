#Script para filtrar por filas 

import pandas as pd

#Definir el max de columnas
max_col=50

#Definiciones de como se debe tomar la informacion para no generar error en pandas
df_raw = pd.read_csv(
    "archivo.txt", 
    sep = "|", #se define el tipo de separador que esta en el archivo 
    header=None, #se establece que no hay encabezados
    dtype = str, #se define que los campos son una cadena de texto
    names=range(max_col), #names hace referencia a las columnas
    on_bad_lines="skip", # Ignora líneas con errores de formato sin mostrar advertencias
    #encoding='latin-1'
    )

dataframe = {}
for tipo in ["R1","R2", "R3", "R4", "R5", "R6"]:
    dataframe[tipo] = df_raw[df_raw[0] == tipo].copy()

df_r1=dataframe["R1"]

df_r1.to_csv(
    "r1.txt",
    index=False,
    sep="|"
)

df_r2=dataframe["R2"]

df_r2.to_csv(
    "r2.txt",
    index=False,
    sep="|"
)

df_r3=dataframe["R3"]

df_r3.to_csv(
    "r3.txt",
    index=False,
    sep="|"
)

df_r4=dataframe["R4"]

df_r4.to_csv(
    "r4.txt",
    index=False,
    sep="|"
)

df_r5=dataframe["R5"]

df_r5.to_csv(
    "r5.txt",
    index=False,
    sep="|"
)

df_r6=dataframe["R6"]

df_r6.to_csv(
    "r6.txt",
    index=False,
    sep="|"
)
