import os

PROJECT_NAME = 'Cross over'
PROJECT_DESC = 'Nullam viverra odio dui ornare suspendisse'
PROJECT_TIME = '7:30 - 17:30 GMT+3'
PROJECT_PHONE = '+7 906 198 3198'
PROJECT_PLACE = 'Neckles Inc., Italy. Napoli. Europe'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'k6o=w6j!)uok2l@dz!u(ec%kg)3yp#hzjk8ntx+oi9^3jn@9yb'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
# INTERNAL_IPS = ('127.0.0.1',)
AUTH_USER_MODEL = 'users.User'
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'compressor',
    'users',
    'core',
    'game',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
ROOT_URLCONF = 'djangoCross.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'core.context_processor.site_meta',
            ],
        },
    },
]
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)
WSGI_APPLICATION = 'djangoCross.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': '405b9c',
        'NAME': 'cross_zero',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
LANGUAGE_CODE = 'ru-RU'
COMPRESS_ENABLED = True
TIME_ZONE = 'Asia/Novosibirsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
STATICFILE_DIRS = (
    os.path.join(BASE_DIR, 'core/static')
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'core/locale'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
MEDIA_URL = '/files/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'
LOGIN_REDIRECT_URL = '/user/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
PAGE_REDIRECT = '/core/'
LOGIN_AFTER_SIGNUP = True
SESSION_ENGINE = 'redis_sessions.session'
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
    }
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
