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

from boto.s3.connection import OrdinaryCallingFormat
from django.utils import six

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

ALLOWED_HOSTS = [
		'admin.mykonosbiennale.com', 
		'mykonosbiennale.org',
		'www.mykonosbiennale.com', 
		'www.mykonosbiennale.org',
		'www.mykonos-biennale.com', 
		'www.mykonos-biennale.org',
		]


# Application definition
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
'django.contrib.sites',
#'django.contrib.sitemaps',
	'storages',
	"compressor",
	'dj_static',
	'django_countries',
	'phonenumber_field',
	'rest_framework',
	'sorl.thumbnail',
	'imagekit',  
	'pipeline',
	're_templatetags',     
	'photologue',
	'sortedm2m',
	'minipub',
	'tagulous',
	    'versatileimagefield',

	#'media_library',
	#'multilingual_tags',
	#'generic_positions',
	#'user_media',
	#'hvad',
	'django_medusa',
	'imagelabs',
	'bakery',
	'variables',
	'pages',
	'material',
	'mykonosbiennale',
	'filmfestival',
	'festival',
	'festivalA',
	'festivaly',
)


MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_DEPLOY_DIR = os.path.abspath(os.path.join(
    'static-sites',
    'var',
    "html"
))

#MEDUSA_COLLECT_STATIC = True

BUILD_DIR = '/home/cabox/workspace/mykonosbiennale.github.io/static-site '
BAKERY_VIEWS = (
    'pages.views.PageView',

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
#'django.middleware.cache.UpdateCacheMiddleware',     
    'django.middleware.common.CommonMiddleware',     
#'django.middleware.cache.FetchFromCacheMiddleware',
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
	  'compressor.finders.CompressorFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
from photologue import PHOTOLOGUE_APP_DIR
PHOTOLOGUE_DIR = 'mykonos-biennale-images'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), PHOTOLOGUE_APP_DIR],
        # note: if you set APP_DIRS to True, you won't need to add 'loaders' under OPTIONS
        # proceeding as if APP_DIRS is False
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
							'django.contrib.auth.context_processors.auth'
            ],
            # start - please add only if APP_DIRS is False
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # end - please add only if APP_DIRS is False
        },
    },
]



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         "NAME": "mb",
#         'USER': 'mb',
#         'PASSWORD': Passwords.db_password, 
#         'HOST': 'elitegrads.cfa2iw0fr9is.us-west-2.rds.amazonaws.com',
#         'PORT': ''
#     }
# }


CACHES_X = {
     'default': {
         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
         'LOCATION': '/home/action/django_cache',
         #'TIMEOUT': 60*60*24,
         'OPTIONS': {
             'MAX_ENTRIES': 1000
         }
     }
 }

CACHES_X = {
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


#
#  S3 static storage
#--------------------------------------------------------------------------

AWS_ACCESS_KEY_ID='AKIAIMB277P23WWWAVAQ'
AWS_SECRET_ACCESS_KEY = Passwords.AWS_SECRET_ACCESS_KEY
#AWS_STORAGE_BUCKET_NAME = 'mykonosbiennale.com'
AWS_STORAGE_BUCKET_NAME = 'com.mykonosbiennale.static'
from S3 import CallingFormat 
AWS_CALLING_FORMAT = CallingFormat.PATH
#AWS_S3_CUSTOM_DOMAIN = 'd1fu8ookpa7iv5.cloudfront.net'

AWS_IS_GZIPPED=True
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7

# TODO See: https://github.com/jschneier/django-storages/issues/47
# Revert the following and use str after the above-mentioned bug is fixed in
# either django-storage-redux or boto
AWS_HEADERS = {
   'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
       AWS_EXPIRY, AWS_EXPIRY))
}
AWS_S3_OBJECT_PARAMETERS = {
   'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
       AWS_EXPIRY, AWS_EXPIRY)),
}
# URL that handles the media served from MEDIA_ROOT, used for managing
# stored files.
MEDIA_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#DEFAULT_FILE_STORAGE = 'mykonosbiennale.s3utils.MediaS3BotoStorage'
# tv STATICFILES_STORAGE = 'mykonosbiennale.s3utils.StaticS3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'



AWS_S3_FILE_OVERWRITE = False

MEDIA_ROOT = '/media/'
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

# STATIC_ROOT = '/static/'
#STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
# tv STATIC_URL = 'https://d1fu8ookpa7iv5.cloudfront.net/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# COMPRESSOR
# ------------------------------------------------------------------------------
# tv COMPRESS_STORAGE = STATICFILES_STORAGE #'storages.backends.s3boto.S3BotoStorage'
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True
COMPRESS_OFFLINE=False




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



TWITTER_APP_KEY = 'O296O2xJdwoTuJM1znUPNexsnX'
TWITTER_APP_SECRET = Passwords.TWITTER_APP_SECRET

THUMBNAIL_DEBUG = False
THUMBNAIL_PREFIX='mykonos-biennale-cache'
import logging
from sorl.thumbnail.log import ThumbnailLogHandler
handler = ThumbnailLogHandler()
handler.setLevel(logging.ERROR)
logging.getLogger('sorl.thumbnail').addHandler(handler)

SERIALIZATION_MODULES = {
    'xml':    'tagulous.serializers.xml_serializer',
    'json':   'tagulous.serializers.json',
    'python': 'tagulous.serializers.python',
    'yaml':   'tagulous.serializers.pyyaml',
}

TAGULOUS_AUTOCOMPLETE_JS = (
    'tagulous/lib/jquery.js',
    'tagulous/lib/select2-3/select2.min.js',
    'tagulous/tagulous.js',
    'tagulous/adaptor/select2.js',
)

TAGULOUS_AUTOCOMPLETE_CSS = {
    'all': ['tagulous/lib/select2-3/select2.css']
}

# Versatile Image Field
VERSATILEIMAGEFIELD_SETTINGS = {
	# The amount of time, in seconds, that references to created images
	# should be stored in the cache. Defaults to `2592000` (30 days)
	'cache_length': 2592000,
	'cache_name': 'versatileimagefield_cache',
	'jpeg_resize_quality': 70,
	'sized_directory_name': '__sized__',
	'filtered_directory_name': '__filtered__',
	'placeholder_directory_name': '__placeholder__',
	'create_images_on_demand': True
}

