# Analizador automático de archivos con VirusTotal 🔍🛡️

Este proyecto en Python permite escanear archivos automáticamente con la API de VirusTotal. Está diseñado para ejecutarse en segundo plano utilizando el **Programador de tareas de Windows**, sin necesidad de intervención manual.

## 🚀 ¿Qué hace este script?

- Escanea un archivo específico (o varios) con la API de VirusTotal.
- Envía el hash o contenido del archivo para verificación.
- Guarda o imprime los resultados del análisis.
- Se ejecuta automáticamente según la programación establecida.

## 🛠️ Requisitos

- Python 3.8 o superior
- Cuenta en [VirusTotal](https://www.virustotal.com/gui/join-us) con API Key
- Conexión a Internet
- Sistema operativo: **Windows 10 o superior**

## 📦 Instalación

1. Clona este repositorio o copia el script a una carpeta local:

   ```bash
   git clone https://github.com/tu-usuario/analizador-virustotal.git
   
2. Instala las dependencias:

       pip install requests

3. Abre el archivo .py y edita la variable API_KEY con tu clave de VirusTotal.
4. Asegúrate de que el archivo a analizar esté en la ruta esperada, o modifica el script para adaptarlo.


## 🔁 Ejecución automática

1. Abre el Programador de tareas (taskschd.msc).
2. Crea una nueva tarea básica.
3. Elige una frecuencia de ejecución (por ejemplo, al iniciar sesión o cada día).
4. En el paso “Iniciar un programa”, selecciona:
5. Marca la opción “Ejecutar con los privilegios más altos”.
6. Guarda la tarea y verifica que se ejecuta correctamente.

## Licencia

Este Proyecto esta bajo una licencia MIT.
