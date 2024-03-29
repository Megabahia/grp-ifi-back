# environ init
import os
import environ
# LIBRERIA FIREBASE
import firebase_admin
from firebase_admin import credentials, firestore

env = environ.Env()

# Establecer el directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tomar variables de entorno del archivo .env
environ.Env.read_env(os.path.join(BASE_DIR, '../GlobalRedPyme/.env.test'))

PRODUCTION=True

#VARIABLES GLOBALES
endpointEmailAsignacionPassword="/grp/asignacionPassword/"
endpointEmailReseteoPassword="/grp/reseteoPassword/"

#VARIABLES VARIAN DE ACUERDO A PRODUCCION O DESARROLLO
if PRODUCTION:
    # URL BACK END
    API_BACK_END = env.str('API_BACK_END')
    API_FRONT_END_CORP_IFIS = env.str('API_FRONT_END_CORP_IFIS')
    API_FRONT_END_BIGPUNTOS = env.str('API_FRONT_END_BIGPUNTOS')
    API_FRONT_END_SANJOSE = env.str('API_FRONT_END_SANJOSE')
    #URL FRONT END
    API_FRONT_END=env.str('API_FRONT_END')
    API_FRONT_END_CENTRAL=env.str('API_FRONT_END_CENTRAL')
    API_FRONT_END_CREDIT=env.str('API_FRONT_END_CREDIT')
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    # CONFIGURACION DE TWILIO
    TWILIO_ACCOUNT_SID = ''
    TWILIO_AUTH_TOKEN = ''

    # CONFIGURACION DE AMAZON S3
    DEFAULT_FILE_STORAGE = env.str('DEFAULT_FILE_STORAGE')
    AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
    # CONFIGURACION DE AMAZON SNS
    AWS_TOPIC_ARN_CODIGOS = env.str('AWS_TOPIC_ARN_CODIGOS')
    AWS_TOPIC_ARN = env.str('AWS_TOPIC_ARN')
    AWS_TOPIC_ARN_MONEDAS = env.str('AWS_TOPIC_ARN_MONEDAS')
    AWS_REGION_NAME = env.str('AWS_REGION_NAME')
    AWS_QUEUE_NAME = env.str('AWS_QUEUE_NAME')
    AWS_QUEUE_NAME_PAGOS = env.str('AWS_QUEUE_NAME_PAGOS')
    AWS_ACCESS_KEY_ID_COLAS = env.str('AWS_ACCESS_KEY_ID_COLAS')
    AWS_SECRET_ACCESS_KEY_COLAS = env.str('AWS_SECRET_ACCESS_KEY_COLAS')
    # CONFIGURACION DE AMAZON TEXTRACT
    AWS_ACCESS_KEY_ID_TEXTRACT = env.str('AWS_ACCESS_KEY_ID_TEXTRACT')
    AWS_SECRET_ACCESS_KEY_TEXTRACT = env.str('AWS_SECRET_ACCESS_KEY_TEXTRACT')
    #CORS
    CORS_ALLOWED_ORIGINS = tuple(env.list('CORS_ALLOWED_ORIGINS'))
    # FIREBASE
    FIREBASE_CRED = credentials.Certificate(os.path.join(BASE_DIR, 'config/serviceAccountKey.json'))
    firebase_admin.initialize_app(FIREBASE_CRED, {"databaseURL": 'grp-sanjose'})
    FIREBASE_DB = firestore.client()
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_central',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_personas_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_personas',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_core_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_core',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_pymes_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_pymes',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_corp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_corp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_mdm_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdm',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_mdp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdp',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_mdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_gdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_gdo',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
        'grp_g_ifi_gde_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_gde',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env.str('MONGODB_ATLAS'),
            },
            'LOGGING': {
                'version': 1,
                'loggers': {
                    'djongo': {
                        'level': 'DEBUG',
                        'propagate': False,                        
                    }
                },
            },
        },
    }
else:
    # URL BACK END
    API_BACK_END = 'http://127.0.0.1:8000/'
    #URL FRONT END
    API_FRONT_END="http://localhost:4203"
    API_FRONT_END_CENTRAL="http://localhost:4201"
    API_FRONT_END_CREDIT="http://localhost:4205"
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    # CONFIGURACION DE TWILIO
    TWILIO_ACCOUNT_SID = ''
    TWILIO_AUTH_TOKEN = ''

    # CONFIGURACION DE AMAZON S3
    DEFAULT_FILE_STORAGE = ''
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_BUCKET_NAME = ''
    #CORS
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ]
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_central',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_personas_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_personas',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_core_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_core',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_pymes_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_pymes',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_corp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_corp',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_mdm_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdm',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_mdp_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdp',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_mdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_mdo',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_gdo_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_gdo',
            'ENFORCE_SCHEMA': False,
        },
        'grp_g_ifi_gde_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_gde',
            'ENFORCE_SCHEMA': False,
        },
    }
