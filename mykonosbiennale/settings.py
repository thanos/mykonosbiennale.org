"""
Django settings for mykonosbiennale project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
APPEND_SLASH=False
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
STATIC_ROOT = os.path.join(PROJECT_ROOT,  "static")
from local_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l^j+suf99qot*94of63$62@(84)qlarmwl315bj4h!u=1x532z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'storages',
    'django_countries',
     'phonenumber_field',
        'rest_framework',
    'sorl.thumbnail',
    'imagekit',  
    'pipeline',
    're_templatetags',
    #'media_library',
    #'multilingual_tags',
    #'generic_positions',
    #'user_media',
    #'hvad',
    'imagelabs',
    'variables',
    'pages',
    'mykonosbiennale',
    'filmfestival',
    'festival',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mykonosbiennale.urls'

WSGI_APPLICATION = 'mykonosbiennale.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
     'pipeline.finders.PipelineFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "mb",
        'USER': 'mb',
        'PASSWORD': Passwords.db_password, 
        'HOST': 'elitegrads.cfa2iw0fr9is.us-west-2.rds.amazonaws.com',
        'PORT': ''
    }
}


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/home/action/django_cache',
#         'TIMEOUT': 60*60*24,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://54.159.35.116:6379/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
print 'STATIC_ROOT',STATIC_ROOT

#
#  S3 static storage
#
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

AWS_ACCESS_KEY_ID='AKIAIMB277P23WWWAVAQ'
AWS_SECRET_ACCESS_KEY = Passwords.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = 'com.mykonosbiennale.static'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
from S3 import CallingFormat 
AWS_CALLING_FORMAT = CallingFormat.PATH




REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.JSONPRenderer',
    ),

    'PAGINATE_BY': 100,
}
"""
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_CSS = {
    'css': {
        'source_filenames': (
          'css/*.css',
          'css/layers.css'
        ),
        'output_filename': 'css/css.css',
    },
}

PIPELINE_ENABLED = True
PIPELINE_JS_COMPRESSOR='pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR=None

PIPELINE_JS = {
    'javascript': {
        'source_filenames': (
          'js/*.js',
        ),
        'output_filename': 'js/js.js',
    }
}

"""
from local_settings import *
