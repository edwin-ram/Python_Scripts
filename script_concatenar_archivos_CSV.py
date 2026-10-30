#Script para concatenar archivos cuando solo uno tiene encabezados y el resto no

import pandas as pd
import glob

total_docs = glob.glob('./inputs/*csv') 

primer_df = pd.read_csv(total_docs[0], sep=",", encoding="utf-8")

columnas_molde = primer_df.columns

lista_dataframes = [primer_df]

for archivo in total_docs[1:]:
    df = pd.read_csv(
        archivo, sep=",", encoding="utf-8", header=None, names=columnas_molde
    )
    lista_dataframes.append(df)

df_consolidado = pd.concat(lista_dataframes, ignore_index=True)


df_consolidado.to_csv("./outputs/archivo_unificado.csv", sep=",", encoding="utf-8", index=False)

