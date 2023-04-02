"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        "https://thich2hand.com/",
        "http://thich2hand.com/",
        "http://www.thich2hand.com/",
        "https://www.thich2hand.com/",
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # -----------Celery-------------------
    'django_celery_results',
    # -----------Cross-origin resource sharing-------------------
    'corsheaders',
    # -----------rest_framework-------------------
    'rest_framework',
    'rest_framework.authtoken',
    # -----------SITE-LIBRARY-------------------
    'django.contrib.sites',
    # -----------THUMBNAIL-LIBRARY-------------------
    'sorl.thumbnail',
    # -----------OAUTH-LIBRARY-------------------
    'social_django',
    # -----------DRF-STUFT-LIBRARY-------------------
    'oauth2_provider',
    'drf_social_oauth2',

    # REPLACE IN FUTURE WITH MY OWN CODE AND PATTERM
    # -----------HEAL-LIBRARY----------
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    'health_check.contrib.celery_ping',         # requires celery
    'health_check.contrib.redis',               # requires Redis broker
    # -----------COUNT-LIBRARY-------------------
    'hitcount',
    # -----------CORE-------------------
    'core',
    'common',
    'user',

    'category', 
    'product',
    'comment',
    'mail',

    'search', 

    # -----------HEAL-------------------
    'healchecker',

    # -----------Swagger-------------------
    'drf_yasg',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', 
]


ROOT_URLCONF = 'app.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
    
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # <=========== CONGIFGURE CELERY ===========>
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# # </========== CONGIFGURE CELERY ===========>

# FOR health_check.db 
REDIS_URL = "redis://redis:6379/0"


# # <=========== CONGIFGURE EMAIL ===========>
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "email")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "emai_pass")
EMAIL_PORT = 587
# # </========== CONGIFGURE EMAIL ===========>

SITE_ID = 1

# import rest_framework.authentication
# # # <=========== CONGIFGURE AUTH ===========>
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    # 'drf_social_oauth2.backends.DjangoOAuth2',
)

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='897327147963-57bk3t7jdkf3o6e25ff8j5srfqlasjjr.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='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'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", "ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", "SECRET KEY")

AUTH_USER_MODEL = 'user.User'

SOCIAL_AUTH_LOGIN_ERROR_URL = 'login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'dashboard'
SOCIAL_AUTH_RAISE_EXCEPTIONS = True

# NEW_USER_REDIRECT_URL = "schema-swagger-ui"

# </========== CONGIFGURE AUTH ===========>

# </========================================================================>
# </============================ REST GO BELOW =============================>
# </========================================================================>


# wonder if this need in my project (# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.)
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

REST_FRAMEWORK = {       
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',

        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        # 'drf_social_oauth2.authentication.SocialAuthentication',
    ),
    # my custom default settings
    'DEFAULT_PAGINATION_CLASS': 'common.my_pagination.SmallResultsSetPagination',
    'DEFAULT_PERMISSION_CLASSES': (
        'common.my_permissions.IsOwnerOrReadOnly',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # throttlleing (https://www.django-rest-framework.org/api-guide/throttling/) use nginx to do this instead of django

}

# allow ip and domain

# set to vietnamese time zone
TIME_ZONE = 'Asia/Ho_Chi_Minh'
# timezone
USE_TZ = True

# # language
# USE_I18N = True

# # location
# USE_L10N = True

ATOMIC_REQUESTS = True

if DEBUG:

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    # INTERNAL_IPS = [
    #     'localhost',
    #     'localhost:8000',
    #     '42.113.187.70',
    #     '192.168.1.17',
    #     '0.0.0.0',
    # ]
    
    # DOCKER IP for debug_toolbar
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
    
    CORS_ALLOWED_ORIGINS = [
        # react port
        'http://localhost:3000',
        # js test
        'http://localhost:6969',
    ]

    STATICFILES_DIRS = [
        '/vol/web/static',
    ]

    SOCIAL_AUTH_ALLOWED_REDIRECT_HOSTS = ['localhost:8000']
else:
    STATIC_ROOT = '/vol/web/static'
    # REAL DOMAIN FOR CORS_ALLOWED_ORIGINS
    print('PRODUCTION')

