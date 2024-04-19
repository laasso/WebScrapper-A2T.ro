import pandas as pd
def generar_ruta_archivo(url, nombre_archivo):
    # Obtener la parte de la URL después del dominio
    ruta_relativa = url.split("//")[-1].split("/", 1)[-1]
    # Agregar el nombre del archivo al final de la ruta
    ruta_archivo_completa = f"../filesCSV/CSV/{ruta_relativa}/{nombre_archivo}.csv"
    return ruta_archivo_completa

def generar_txt_desde_csv(nombre_archivo_csv, nombre_archivo_txt):
    # Leer el CSV
    df = pd.read_csv(nombre_archivo_csv)
    # Escribir la información en el archivo de texto
    with open(nombre_archivo_txt, 'w') as file:
        for url in df['URL']:
            ruta_csv = generar_ruta_archivo(url, nombre_archivo_csv)
            file.write(f"{url}, {ruta_csv}\n")

# Ejemplo de uso
nombre_archivo_csv = "/home/lasso/WebScrapper-A2T.ro/filesCSV/CSVurls/URLS.csv"
nombre_archivo_txt = "/home/lasso/WebScrapper-A2T.ro/INFO/informacion.txt"
generar_txt_desde_csv(nombre_archivo_csv, nombre_archivo_txt)
