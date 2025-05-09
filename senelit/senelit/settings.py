import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------
# 1) SECRET_KEY
# ----------------------------------------
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-)fv+6nawk9ef)-aw2_(pp7ui%4*n4yq44t*rrih8*ic8mm=ipp'
)

# ----------------------------------------
# 2) DEBUG
# ----------------------------------------
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ----------------------------------------
# 3) ALLOWED_HOSTS
# ----------------------------------------
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# ----------------------------------------
# Installed apps
# ----------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# ----------------------------------------
# Middleware
# ----------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',            # WhiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'senelit.urls'

# ----------------------------------------
# Templates (necesario para el admin)
# ----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # carpeta global de plantillas (opcional)
        'APP_DIRS': True,                   # busca templates/ en cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'senelit.wsgi.application'

# ----------------------------------------
# Base de datos (SQLite)
# ----------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------
# Archivos estáticos (WhiteNoise)
# ----------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Permite HTTPS tras el proxy de Render
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ----------------------------------------
# Default primary key field type
# ----------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
