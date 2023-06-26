import os
from os.path import join
from distutils.util import strtobool
import dj_database_url
from configurations import Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    INSTALLED_APPS = (
        'modeltranslation',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints
        'drf_yasg',  

        # Your apps
        'apps.news',
        'apps.contact',
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = 'config.urls'
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'config.wsgi.application'

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    ADMINS = (
        ('Author', 'sevbofx@gmail.com'),
    )

    # Postgres
    if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': join(BASE_DIR, 'db.sqlite3'),
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('POSTGRES_DB'),
                'USER': os.getenv('POSTGRES_USER'),
                'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
                'HOST': '127.0.0.1',
                'PORT': 5432,
            }
        }

    # General
    APPEND_SLASH = True
    TIME_ZONE = 'Asia/Tashkent'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
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



    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
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

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Custom user app

    # Django Rest Framework
    REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'core.paginations.CustomPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
}

    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://localhost:6379/0',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }

    # Celery settings
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'
    # SAVE SESSION IN PRODUCTION
    # SESSION_COOKIE_DOMAIN = 'backend.stroymarkets.uz'
    SESSION_SAVE_EVERY_REQUEST = True

    MAIN_DOMAIN = os.getenv('MAIN_DOMAIN', 'http://127.0.0.1:8000')
    ADMIN_PATH = os.getenv('ADMIN_PATH', 'hello-admin')

    gettext = lambda s: s
    LANGUAGES = (
        ('en', gettext('English')),
        ('ru', gettext('Russian')),
        ('uz', gettext('Uzbek')),
    )

    MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')
    MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

    CORS_ORIGIN_ALLOW_ALL = True
    # CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST').split()
    # CORS_ORIGIN_REGEX_WHITELIST = [
    #     '%r' % value
    #     for value in getenv('CORS_ORIGIN_REGEX_WHITELIST', type=list, default=[])
    # ]
    # CORS_ALLOW_HEADERS = getenv(
    #     'CORS_ALLOW_HEADERS', type=list, default=list(default_headers)
    # )
    # CORS_ALLOW_METHODS = getenv(
    #     'CORS_ALLOW_METHODS', type=list, default=list(default_methods)
    # )

    ESKIZ_EMAIL = os.getenv('ESKIZ_EMAIL', 'None')
    ESKIZ_PASSWORD = os.getenv('ESKIZ_PASSWORD', 'None')
    

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))