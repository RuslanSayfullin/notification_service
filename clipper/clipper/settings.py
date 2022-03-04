"""
Django settings for clipper project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

from .settings_db_debug import DEBUG, DATABASES  # импорт настроект "режима отладки" и "базы данных"
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+x)f@vva()@)ln8om_x!4+gwl=g%l#zm573=hh9@aqdm4*75#+'

ALLOWED_HOSTS = ['clipper-commerce.ru', 'localhost', '127.0.0.1']

# Настройки REDIS
REDIS_HOST = ['*']
REDIS_PORT = 6379
REDIS_DB = 0
# /Настройки REDIS


INTERNAL_IPS = (
    "127.0.0.1",
)

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'social_django',
    'sorl.thumbnail',
]+['blog.apps.BlogConfig',
   'account.apps.AccountConfig',
   'images.apps.ImagesConfig',
   'actions.apps.ActionsConfig',
   'shop.apps.ShopConfig',
   'cart.apps.CartConfig',
   'orders.apps.OrdersConfig',
   'payment.apps.PaymentConfig',
   ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'clipper.urls'

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
                'cart.context_processors.cart',     # Добавление корзины в контекст шаблонов
            ],
        },
    },
]

WSGI_APPLICATION = 'clipper.wsgi.application'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# рассылка служебных сообщений на e-mail
EMAIL_HOST = 'smtp.gmail.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'mrcrownt@gmail.com'
EMAIL_HOST_PASSWORD = '14121987_Aletta_Ocean'
DEFAULT_FROM_EMAIL = u'Уведомление Портала <mrcrownt@gmail.com>'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Аутентификация Facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'XXX'    # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX'     # Facebook App Secret

# Аутентификация Twitter
SOCIAL_AUTH_TWITTER_KEY = 'XXX'     # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'XXX'  # Twitter Consumer Secret

# Аутентификация Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXX'   # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX'    # Google Consumer Secret

from django.urls import reverse_lazy
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}

# ключ, по которому мы будем хранить данные корзины покупок в сессии, интернет магазина
CART_SESSION_ID = 'cart'

# Настройки Braintree.
BRAINTREE_MERCHANT_ID = 'XXX' # ID продавца.
BRAINTREE_PUBLIC_KEY = 'XXX' # Публичный ключ.
BRAINTREE_PRIVATE_KEY = 'XXX' # Секретный ключ.

from braintree import Configuration, Environment

Configuration.configure(
Environment.Sandbox,
BRAINTREE_MERCHANT_ID,
BRAINTREE_PUBLIC_KEY,
BRAINTREE_PRIVATE_KEY
)
# /Настройки Braintree.
