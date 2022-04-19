PRODUCTION=True

#VARIABLES GLOBALES
endpointEmailAsignacionPassword="/grp/asignacionPassword/"
endpointEmailReseteoPassword="/grp/reseteoPassword/"

#VARIABLES VARIAN DE ACUERDO A PRODUCCION O DESARROLLO
if PRODUCTION:
    # URL BACK END
    API_BACK_END = '209.145.61.41:8003/'
    #URL FRONT END
    API_FRONT_END="http://209.145.61.41:4203"
    API_FRONT_END_CENTRAL="http://209.145.61.41:4206"
    API_FRONT_END_CREDIT="http://209.145.61.41:4209"
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
        "http://209.145.61.41:4206",
        "http://209.145.61.41:4207",
        "http://209.145.61.41:4208",
        "http://209.145.61.41:4209",
    ]
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_g_ifi_central',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
                'host': '209.145.61.41',
                'port': 27017,
                'username': 'usr_testing',
                'password': 'FAiK&OgZpP8^',
                'authSource': 'admin',
                'authMechanism': 'SCRAM-SHA-1'
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
