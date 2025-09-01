# 📊 Estado del build (badge) 

### (Se agrega por trabajo de implantación - automatización con Github actions) 

![Django Tests](https://github.com/Leyly123/ApiCandySoft/actions/workflows/django-tests.yml/badge.svg)

**⚠️ Lo anterior es una imagen dinámica que GitHub genera automáticamente.**

#### 📌Muestra el estado de tu workflow (django-tests.yml).

- Tiene tres estados posibles:

  - ✅ verde → las pruebas pasaron.

  - ❌ rojo → alguna prueba falló.

  - 🔄 amarillo → está en ejecución.

---

# 🍬 API Candy Soft - Proyecto Modularizado (Trabajo de prueba)

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

# 2.1. En el archivo settings.py de la carpeta apiCandySoft, entre las líneas 118 y 128 se encuentra la configuración de la base de datos dentro del diccionario DATABASES.

# Actualmente, el bloque de código luce así:

DATABASES = {
    'default':{
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
} 

# A esta configuración se le debe agregar la sección OPTIONS para especificar el uso del conjunto de caracteres utf8mb4, que permite un manejo más completo de caracteres especiales y emojis en la base de datos.

'OPTIONS': {
    'charset' : 'utf8mb4',
}

# El bloque de configuración actualizado quedaría de la siguiente forma:

DATABASES = {
    'default':{
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'OPTIONS': {
          'charset' : 'utf8mb4',
        }
    }
}

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
# - Ejecuta este comando (SQL)
CREATE DATABASE CandySoftApi2;

# Luego, importar el archivo db_candysoft.sql en la base de datos:
# Despues de crear la base de datos, vuelve a la terminal del proyecto (PowerShell) la misma con la que venias ejecutando
# ⚠️ Nota: en la parte -p --port=3307, el proyecto está configurado en 3307, si tu MySQL corre en 3306 cámbialo.
# Ejecuta el comando
# Te pedira la contraseña de tu MySQL (si tiene)
Get-Content db_candysoft.sql | & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p --port=3307 CandySoftApi2


# 7. Ingresar a la carpeta principal donde está manage.py
cd apiCandySoft

# 8. (OPCIONAL - SOLO SI EL SQL NO DIO) Migrar base de datos con Django
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

```
---

# ✅ Automatización de pruebas con GitHub Actions (Trabajo implantación)

Este proyecto cuenta con un flujo de integración continua (CI) configurado con GitHub Actions.
Cada vez que haces un push o un pull request hacia la rama main, se ejecutan automáticamente las pruebas unitarias del proyecto.

---

## 📂 Ubicación del workflow

El flujo se encuentra en el archivo:

```bash

.github/workflows/django-tests.yml

```

---

## 🔧 ¿Qué hace el workflow?

- Configura un entorno en Ubuntu.

- Levanta un servicio de PostgreSQL 14 (antes era MySQL 8.0, ya se actualizó).

- Instala Python 3.10.

- Instala las dependencias desde requirements.txt.

- Configura las variables de entorno de Django (simulando lo que está en el .env).

- Usa la variable DATABASE_URL para conectarse a la base de datos de pruebas en PostgreSQL.

- Ejecuta las migraciones con python manage.py migrate.

- Corre todas las pruebas unitarias con python manage.py test.

---

## 🚀 Resultado

- Si las pruebas pasan ✅, GitHub marca el commit o PR como exitoso.

- Si alguna prueba falla ❌, el flujo se detiene y verás el error en la pestaña Actions de GitHub.

**📌 Nota importante**

- En GitHub Actions, la base de datos se crea con migrate (sin usar el archivo db_candysoft.sql).

- En tu PC local, puedes usar db_candysoft.sql para cargar datos de ejemplo más rápido.

---

👉 [Ver ejecuciones en GitHub Actions](https://github.com/Leyly123/ApiCandySoft/actions)

**📌 Nota importante**

Ese enlace abre la pestaña **Actions** del repositorio, donde podrás ver:

- Ver todas las ejecuciones pasadas del flujo `django-tests.yml`.
- Revisar si un commit pasó o falló las pruebas.
- Consultar los logs detallados de cada paso del workflow.
