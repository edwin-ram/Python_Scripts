#Script para comprimir en zip documentos de diferentes carpetas (path) y renomnbrar las carpetas resultantes

from pathlib import Path
import pandas as pd
import zipfile

directorio_origen_pdf = Path("ruta/origen/archivosA")
directorio_origen_xml = Path("ruta/origen/archivosB")
directorio_destino_PREMIUM = Path("ruta/destino/archivosZIP")

df_doc = pd.read_csv('Documentos_facturados.csv', sep = '|')

for index, fila in df_doc.iterrows():

    cufe = str(fila['CUFE']).strip()
    factura = str(fila['FACTURA']).strip()
    contrato = str(fila['CONTRATO']).strip()

    nombre_compuesto_factura = f"Plan Premium_Factura_{factura}_{contrato}"

    carpeta_zip = f"{nombre_compuesto_factura}.zip"
    ruta_destino = directorio_destino_PREMIUM / carpeta_zip

    pdf_docs = list(directorio_origen_pdf.glob(f"{cufe}*"))
    xml_docs = list(directorio_origen_xml.glob(f"{cufe}*"))


    if pdf_docs or xml_docs:
        with zipfile.ZipFile(ruta_destino, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
            for archivo in pdf_docs:
                if archivo.is_file:
                    nuevo_nombre_pdf = f"{nombre_compuesto_factura}.pdf"
                    archivo_zip.write(archivo, arcname = nuevo_nombre_pdf)

            for archivo in xml_docs:
                if archivo.is_file:
                    archivo_zip.write(archivo, arcname=archivo.name)

print("Proceso finalizado de manera exitosa")