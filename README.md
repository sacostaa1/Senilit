# 📌 Senilit  
**Plataforma de anuncios estudiantiles con diseño moderno y modo "Corcho TV"**  

## Pagina principal de la HU
![image](https://github.com/user-attachments/assets/fab4f2cc-b2d4-491a-9500-b9664fee3983)

# 📌 Plataforma de Servicios Universitarios

Este proyecto es una plataforma web que permite a los estudiantes de la universidad visualizar y explorar diferentes servicios organizados por categorías como Académico, Bienestar, Eventos, Deportes, Cultura, Tecnología, Emprendimiento y Salud.

## ✨ Características principales

📂 Listado de servicios organizados en categorías configurables.
🔍 Búsqueda rápida y navegación intuitiva.
📄 Información detallada de cada servicio (nombre, descripción).
⭐ Funcionalidad para agregar y gestionar favoritos sin autenticación.
🖥️ Diseño adaptable para pantallas grandes y pequeñas.

## 📊 Datos

La información de los servicios y categorías se obtiene desde archivos CSV, lo que permite fácil actualización sin necesidad de modificar la base de datos directamente.

## ⚙️ Tecnologías utilizadas

🐍 Python con Django para el backend.
🗄️ CSV como fuente de datos.
🌐 HTML y CSS para la interfaz de usuario.
📌 JavaScript para la gestión de favoritos dinámicamente.

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:
   

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # En Windows
   ```

3. Ejecuta las migraciones y corre el servidor:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. Accede a la plataforma en el navegador:
   - **Favoritos:** [http://127.0.0.1:8000/favorites/](http://127.0.0.1:8000/favorites/)
