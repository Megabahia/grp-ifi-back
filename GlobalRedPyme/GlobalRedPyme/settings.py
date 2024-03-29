"""
Django settings for GlobalRedPyme project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import environ
from pathlib import Path
import os
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from apps.config import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# environ init
env = environ.Env()
environ.Env.read_env() # LEE ARCHIVO .ENV

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Corp
    'apps.CORP.corp_cobrarSupermonedas',
    'apps.CORP.corp_autorizaciones',
    'apps.CORP.corp_movimientoCobros',
    'apps.CORP.corp_pagos',
    'apps.CORP.corp_creditoPersonas',
    'apps.CORP.corp_creditoPreaprobados',
    'apps.CORP.corp_notasPedidos',
    'apps.CORP.corp_monedasEmpresa',
    'apps.CORP.corp_creditoArchivos',
    'apps.CORP.corp_envios',
    'apps.CORP.corp_firmaElectronica',
    'apps.CORP.corp_pagoProveedores',
    # Pymes
    'apps.CORP.corp_empresas',
    # apps core
    'apps.CORE.core_monedas',
    # apps personas
    'apps.PERSONAS.personas_personas',
    'apps.PERSONAS.personas_historialLaboral',
    'apps.PERSONAS.personas_rucPersonas',
    'apps.PERSONAS.personas_proveedores',
    #apps central CENTRAL
    'apps.CENTRAL.central_logs',
    'apps.CENTRAL.central_roles',
    'apps.CENTRAL.central_usuarios',
    'apps.CENTRAL.central_autenticacion',
    'apps.CENTRAL.central_acciones',
    'apps.CENTRAL.central_catalogo',
    'apps.CENTRAL.central_facturas',
    'apps.CENTRAL.central_infoUsuarios',
    'apps.CENTRAL.central_productos',
    'apps.CENTRAL.central_publicaciones',
    'apps.CENTRAL.central_tipoUsuarios',
    'apps.CENTRAL.central_correosLanding',
    #apps vittoria MDM+
    'apps.MDM.mdm_clientes',
    'apps.MDM.mdm_facturas',
    'apps.MDM.mdm_negocios',
    'apps.MDM.mdm_prospectosClientes',
    #apps Vittoria MDP
    'apps.MDP.mdp_categorias',
    'apps.MDP.mdp_subCategorias',
    'apps.MDP.mdp_productos',
    'apps.MDP.mdp_fichaTecnicaProductos',    
    # apps Vittoria MDO
    'apps.MDO.mdo_prediccionCrosseling',
    'apps.MDO.mdo_prediccionRefil',
    'apps.MDO.mdo_prediccionProductosNuevos',
    'apps.MDO.mdo_generarOferta',
    # apss Vittoria GDO
    'apps.GDO.gdo_gestionOferta',
    # apps vittoria GDE
    'apps.GDE.gde_gestionEntrega',
    #Django external apps
    'corsheaders',
    'rest_framework',
    'django_rest_passwordreset',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'drf_yasg',
    'django_crontab',
]

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.CENTRAL.central_autenticacion.auth.ExpiringTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'GlobalRedPyme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'GlobalRedPyme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = config.DATABASES

#AGREGO LAS RUTAS DE LAS DIFERENTES BASES DE DATOS
DATABASE_ROUTERS = [
    'apps.config.routersDB.GRPPERSONASRouter',
    'apps.config.routersDB.GRPCORERouter',
    'apps.config.routersDB.GRPCORPRouter',
    'apps.config.routersDB.MDMRouter',
    'apps.config.routersDB.MDPRouter',
    'apps.config.routersDB.MDORouter',
    'apps.config.routersDB.GDORouter',
    'apps.config.routersDB.GDERouter',
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = "central_usuarios.Usuarios"
#TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
TOKEN_EXPIRED_AFTER_SECONDS = env.int('TOKEN_EXPIRED_AFTER_SECONDS')
#NOMBRE KEYWORK TOKEN
TOKEN_KEYWORD= env.str('TOKEN_KEYWORD')
# Config Email
# EMAIL_BACKEND = env.str('EMAIL_BACKEND')
# EMAIL_HOST = env.str('EMAIL_HOST')
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = env.int('EMAIL_PORT')
#CORS
# CORS_ALLOWED_ORIGINS = tuple(env.list('CORS_ALLOWED_ORIGINS', default=[]))
CORS_ALLOWED_ORIGINS = config.CORS_ALLOWED_ORIGINS

SILENCED_SYSTEM_CHECKS = ['auth.E003', 'auth.W004']

# CONFIGURACION DE TWILIO
TWILIO_ACCOUNT_SID = env.str('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = env.str('TWILIO_AUTH_TOKEN')

# CONFIGURACION DE AMAZON S3
DEFAULT_FILE_STORAGE = env.str('DEFAULT_FILE_STORAGE')
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False 


CRONJOBS = [
    # La función temporizada se ejecuta cada minuto
    # ('*/1 * * * *', 'apps.CORP.corp_pagos.cron_ifi.hi'),
    ('*/1 * * * *', 'apps.CORP.corp_creditoPersonas.consumer_ifi.get_queue_url'),
    # ('*/1 * * * *', 'apps.CORP.corp_pagos.consumer_pagos.get_queue_url'),
]