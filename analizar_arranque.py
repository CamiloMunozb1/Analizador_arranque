import os # Libreria os para manejo de archivos
import time # Libreria time para detener el programa
import requests # Libreria request para hacer consultas
import winshell # Libreria winshell para acceder a carpetas especiales


# API KEY de virustotal.
api_key = r"TU_API_KEY"
# Carpeta de archivo a analizar.
archivo_arranque = r"CARPETA_ANALIZAR"
# URL para peticiones a virustotal.
url = "https://www.virustotal.com/api/v3/files"
# Achivo JSon de subida.
headers = {
    "x-apikey" : api_key
}
# Se busca por cada archivo dentro de la carpeta.
for file in os.listdir(archivo_arranque):
    # Se busca el valor en especifico.
    if file.endswith('.lnk'):
        # Añade el valor especifico al archivo.
        shortcut_path = os.path.join(archivo_arranque,file)
        # Busqueda eb carpeta especial.
        winshell_path = winshell.shortcut(shortcut_path)
        # Toma de archivos ".exe".
        exe_path = winshell_path.path
        # Busqueda de archivos exe.
        if os.path.isfile(exe_path) and exe_path.endswith(".exe"):
            # Modo de lectura de los archivos.
            with open(exe_path, "rb") as f:
                # Estructura de subida de los archivos ".exe" a virustotal
                file = {
                    "file" : (os.path.basename(exe_path),f)
                }
                # Tiempo de espera de 5 segundos entre cada archivo para no saturar las peticiones.
                time.sleep(5)
                # Metodo post para subir los archivos seleccionados.
                file_json = requests.post(url, files=file, headers=headers)
                # Se buscan los campos especificos en el archivo Json
                analisis_id = file_json.json()["data"]["id"]
                # Busqueda de datos analizados.
                analisis_url = f"https://www.virustotal.com/api/v3/analyses/{analisis_id}"
                # Respuesta de estos archivos analidados en archivos Json.
                respuesta_json = requests.get(analisis_url, headers=headers)
                # Visalizacion de los datos.
                print(respuesta_json.json())