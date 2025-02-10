# 📌 Proyecto: Plataforma de Calificación de Servicios

Este proyecto es una aplicación web desarrollada en **Django** que permite a los usuarios calificar servicios y dejar reseñas. Se requiere autenticación para poder calificar un servicio.

---

## 🚀 **Instalación y Configuración**

### **1️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/tu-repositorio.git
cd tu-repositorio
```

### **2️⃣ Crear y Activar el Entorno Virtual**
```bash
python -m venv .venv  # Crear el entorno virtual
source .venv/bin/activate  # En macOS/Linux
.venv\Scripts\activate  # En Windows
```

### **3️⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar la Base de Datos**
```bash
python manage.py migrate  # Aplicar las migraciones
python manage.py createsuperuser  # (Opcional) Crear un usuario administrador
```

### **5️⃣ Ejecutar el Servidor de Desarrollo**
```bash
python manage.py runserver
```

El servidor iniciará en: **http://127.0.0.1:8000/**

---

## 🌟 **Cómo Usar la Plataforma**

### 🔹 **Registro e Inicio de Sesión**
- Para iniciar sesión, accede a **http://127.0.0.1:8000/**
- Usuario: UsuarioProfesor
- Password: UsuarioProfesor
- Para registrarte, contacta con el administrador (no hay registro público habilitado).

### 🔹 **Calificar un Servicio**
1. Accede a **http://127.0.0.1:8000/calificar/1/** (Reemplaza `1` por el ID del servicio).
2. Selecciona una calificación de **1 a 5 estrellas**.
3. (Opcional) Escribe una reseña.
4. Haz clic en "Enviar Calificación".
5. Serás redirigido a **http://127.0.0.1:8000/servicio/1/** donde verás todas las calificaciones.

### 🔹 **Panel de Administración**
Si tienes permisos de administrador, accede a **http://127.0.0.1:8000/admin/** para gestionar los servicios y usuarios.

---

## 🛠 **Estructura del Proyecto**
```
📂 myapp/                 # Aplicación principal
│── 📂 migrations/        # Migraciones de la base de datos
│── 📂 templates/         # Archivos HTML
│── 📂 static/            # Archivos CSS y JS (si se usan)
│── 📄 views.py           # Lógica de las vistas
│── 📄 models.py          # Definición de la base de datos
│── 📄 urls.py            # Rutas de la aplicación
│── 📄 forms.py           # Formularios (si aplica)
📂 senelit/               # Configuración global del proyecto
│── 📄 settings.py        # Configuración de Django
│── 📄 urls.py            # Rutas globales
│── 📄 wsgi.py            # Configuración para producción
📄 manage.py              # Archivo principal para ejecutar comandos de Django
📄 requirements.txt       # Lista de dependencias
📄 README.md              # Documentación del proyecto
```

---

## 🛠 **Tecnologías Utilizadas**
- 🐍 **Django 5.1.0** (Framework web en Python)
- 🛢 **SQLite** (Base de datos por defecto en Django)
- 🎨 **HTML, CSS** (Para la interfaz de usuario)
- 🔑 **Autenticación de Django** (Para gestión de usuarios)

---

## 🤝 **Contribuciones**
Si deseas contribuir al proyecto, sigue estos pasos:
1. **Haz un fork** del repositorio.
2. **Crea una nueva rama** con tu mejora:
   ```bash
   git checkout -b mi-nueva-rama
   ```
3. **Realiza tus cambios y confirma los commits:**
   ```bash
   git commit -m "Descripción de la mejora"
   ```
4. **Sube los cambios a tu fork:**
   ```bash
   git push origin mi-nueva-rama
   ```
5. **Crea un Pull Request** desde GitHub.

---

## 📧 **Contacto**
Si tienes dudas o sugerencias, puedes abrir un **issue** en GitHub o contactarme en mi correo 📩 **jcramonp@eafit.edu.co**.

🚀 ¡Gracias por contribuir y usar esta plataforma! 🎉

