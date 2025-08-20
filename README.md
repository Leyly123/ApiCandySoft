# 🍬 API Candy Soft - Proyecto Modularizado

Este proyecto corresponde a una **API REST en Django** para la gestión de un sistema modularizado.  
A continuación encontrarás los pasos exactos para clonar, configurar, instalar dependencias, importar/migrar la base de datos, correr pruebas y levantar el servidor.  

---

## ⚙️ Requisitos previos

Antes de comenzar, asegúrate de tener instalado en tu equipo:

- **[Python 3.10+](https://www.python.org/downloads/)** → Lenguaje de programación principal.  
- **[MySQL](https://dev.mysql.com/downloads/installer/)** → Base de datos relacional utilizada por el proyecto.  
- **[Git](https://git-scm.com/downloads)** → Para clonar y gestionar el repositorio.  

Opcional (pero recomendado):  
- **Visual Studio Code** → Editor de código que facilita la ejecución y depuración.  

---

## 🎀 Explicación del proyecto Candy Soft

Candy Soft es un sistema modularizado desarrollado en Django que busca optimizar la gestión de un spa de uñas. De esta forma, facilita el control de los recursos, mejora la organización de la información y asegura un flujo de trabajo más eficiente dentro del negocio.

---

## 🧩 Explicación de los módulos y clases con pruebas

- **Módulo y clase marca** → Representa la categoría o empresa que fabrica o comercializa un insumo.  
- **Módulo y clase insumo** → Corresponde a los productos utilizados para la prestación de los servicios. Se llaman “insumos” porque no se venden de manera individual, sino que se emplean únicamente durante la ejecución de los servicios.  
- **Módulos y clases cliente, manicurista, usuario** → Son las personas y roles que tienen acceso al aplicativo.  
  - En **usuario** se registran tanto administradores como recepcionistas, ya que requieren los mismos datos.  
  - En **manicurista** y **cliente** se solicitan datos adicionales y diferentes, específicos para cada caso.  

---

## 🚀 Instalación y despliegue

```bash
# 1. Clonar el repositorio

# ➡️ Opción 1: Clonar desde GitHub (recomendado)
# Entra al repositorio en GitHub y da clic en el botón <> Code
# Copia el enlace HTTPS que aparece
# En VS Code, abre el ícono de Source Control (Control de código fuente)
# Haz clic en "Clonar repositorio", pega el enlace y acepta
# Selecciona la carpeta donde quieres guardarlo

# ➡️ Opción 2: Descargar ZIP
# Entra al repositorio en GitHub y da clic en el botón <> Code
# Selecciona "Download ZIP"
# Descomprime el archivo y ábrelo en VS Code

# ➡️ Opción 3: Línea de comandos
git clone https://github.com/Leyly123/ApiCandySoft.git
cd ApiCandySoft


# 2. Crear archivo .env
# - Crealo dentro de la carpeta apiCandySoft, se debe llamar asi .env
# - Copia y pega el siguiente código
# - En la línea 9 cambia la contraseña de MySQL (DB_PASSWORD) por la que tengas configurada en tu máquina.
# - Si tu usuario no tiene contraseña, deja el valor vacío.
# - En la línea 11 revisa el puerto de conexión a MySQL (DB_PORT).
#   El proyecto está configurado en 3307, si tu MySQL corre en 3306 cámbialo.

# Este es el código que debes copiar y pegar en el archivo .env

SECRET_KEY='django-insecure-$=ae#$xpmjkw=7v&&0kv@$a)j+o9ti%u%z+tygd#3nzju=pajc'
DEBUG=True

#base de datos - solo cambia esto

DB_ENGINE=django.db.backends.mysql
DB_NAME='CandySoftApi2'
DB_USER=root
DB_PASSWORD='tu-contraseña*'
DB_HOST=127.0.0.1
DB_PORT=3307


#tema de correo - esto dejarlo igual
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'candysoftpruebaapi@gmail.com'
EMAIL_HOST_PASSWORD = 'ikyp huvb lnia zekw'

IMGBB_API_KEY = "fec1ba28d181c77a5801a0952fead016"

# Hasta aqui el código que debes de copiar y pegar.

# Abre la terminal (PowerShell) y ejecuta los siguientes comandos en este orden

# 3. Crear entorno virtual
python -m venv venv

# 4. Activar entorno virtual (en PowerShell)
.\venv\Scripts\activate

# 5. Instalar dependencias
pip install -r requirements.txt


# 6. Importar base de datos con el archivo SQL

# Primero, crear la base de datos vacía en MySQL (si no existe):
# - Abre MySQL
# - Ejecuta este comando
CREATE DATABASE CandySoftApi2;

# Luego, importar el archivo db_candysoft.sql en la base de datos:
# ⚠️ Nota: en la parte -p --port=3307, el proyecto está configurado en 3307, si tu MySQL corre en 3306 cámbialo.
Get-Content db_candysoft.sql | & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p --port=3307 CandySoftApi2


# 7. Ingresar a la carpeta principal donde está manage.py
cd apiCandySoft

# 8. (OPCIONAL) Migrar base de datos con Django
# ⚠️ Solo usa este comando si no funcionó la importación con el archivo SQL.
python manage.py migrate


# 9. Ejecutar pruebas unitarias
# ⚠️ Nota: después de ejecutar cada prueba es necesario cambiar los datos de entrada,
# porque ya quedan guardados en la base de datos y puede generarse error por duplicados.

# Módulo insumo (carpeta insumo/tests/)
python manage.py test insumo.tests.test_marca
python manage.py test insumo.tests.test_insumo

# Módulo usuario (carpeta usuario/tests/)
python manage.py test usuario.tests.test_manicurista
python manage.py test usuario.tests.test_usuario
python manage.py test usuario.tests.test_cliente


# 10. Levantar servidor de desarrollo
python manage.py runserver
