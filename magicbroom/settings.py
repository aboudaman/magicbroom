"""
Django settings for magicbroom project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set Internatl IP

INTERNAL_IP = ['127.0.0.1', '192.168.0.6']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Set Django mode
DJANGO_MODE = os.getenv('DJANGO_MODE', "Production").lower()

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '0+jas=_#1wfp%0#k=xpr_+wwvg+lg7o4vva189t5cy-md_bgt('
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_MODE == 'local':
    DEBUG = True
else:
    DEBUG = False



# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party app
    'localflavor',
    'phonenumber_field',
    'multiselectfield',

    # custom apps
    'magicbroomsite.apps.MagicbroomsiteConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'magicbroom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'magicbroom', 'templates')],
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

WSGI_APPLICATION = 'magicbroom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DJANGO_MODE == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif DJANGO_MODE == 'staging':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('USER'),
            'PASSWORD': os.getenv('PASSWORD'),
            'HOST': os.getenv('HOST', '127.0.0.1'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
elif DJANGO_MODE == 'production':
    import dj_database_url
    # Handle database url environment variable for production
    DATABASES = {
        'default': dj_database_url.config()

        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_INPUT_FORMATS = ['%I:%M %p',]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Collect all static files
STATIC_ROOT = 'staticfiles'

# Define static files location
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'magicbroom', 'static'),
)

# Set Up Email Functionality
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'aboudaman'
EMAIL_HOST_PASSWORD = '#########'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
