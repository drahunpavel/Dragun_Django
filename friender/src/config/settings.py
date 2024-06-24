"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv

# относительный путь
dotenv_path = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), '..', '.env')
load_dotenv(dotenv_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-tu*l=6%kq%6z2w*sg+ybrdiq6mr)@e-7b09$04i!r%9zlt&-5b'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = False
DEBUG = os.environ.get("DEBUG")

# todo по дефолту localhost
# ALLOWED_HOSTS = ['*']


# Application definition

# todo Коробочное решение от django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'booking_service',
    'booking_rest_api',
    'booking_auth_api',
    'phonenumber_field',
    'bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'django_celery_results'
]

REST_FRAMEWORK = {
    # todo настройка для работы с токенами
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
     # todo настройка для фильттрации данных
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    # todo настройка глобальной пагинации  (применяет пагинацию ко всем API-представлениям, которые возвращают списки объектов)
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),  #todo Время жизни access-токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    #todo Время жизни refresh-токена
    'AUTH_HEADER_TYPES': ('Bearer',),
}

#  Bootstrap 5 в качестве шаблона для crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/booking_service'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASS"),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '5432'),
        # "TEST": {
        #     "NAME": "test_arrangements",
        # },
    },
    'test': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME_TEST"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASS"),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#todo Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INTERNAL_IPS = [
    "127.0.0.1",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


# CACHES: dict[str, dict[str, str]] = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # кэширование БД
#         'LOCATION': 'my_cache_table',
#     },
#     'filesystem': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }


# todo настройка для автоинкрементированных ключей. Если используются uuid - не нужна
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#todo Celery

CELERY_BROKER_URL = 'amqp://localhost'  # URL брокера RabbitMQ
CELERY_RESULT_BACKEND = 'django-db'  # Использование базы данных Django для хранения результатов задач

# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = '6379'
# CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ":" + REDIS_PORT + '/0'
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_IMPORTS = ('booking_service.tasks',) # Путь к  задачам Celery


# Настройки Flower
FLOWER_PORT = 5555  # Порт для Flower