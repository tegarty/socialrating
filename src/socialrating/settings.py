"""
Django settings for socialrating project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import wrapt
import django.views
from django.contrib.staticfiles.templatetags.staticfiles import static

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# import local settings
from .environment_settings import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # needed for allauth

    'eav',
    'bootstrap4',
    #'django_extensions',
    'django_db_log_requestid',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'actor',
    'team',
    'category',
    'context',
    'fact',
    'item',
    'review',
    'rating',
    'utils',
    'eventlog',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'socialrating.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'team.context_processors.team',
            ],
        },
    },
]

WSGI_APPLICATION = 'socialrating.wsgi.application'
ASGI_APPLICATION = "socialrating.routing.application"

AUTH_USER_MODEL = 'actor.User'
LOGIN_REDIRECT_URL = '/'

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True

# static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_src')] # find static files here
STATIC_ROOT = os.path.join(BASE_DIR, "static") # collect static files here
STATIC_URL = '/static/' # serve static files here

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'syslog': {
            'format': '%(levelname)s %(name)s.%(funcName)s(): %(message)s'
        },
        'console': {
            'format': '[%(asctime)s] %(name)s.%(funcName)s() %(levelname)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'socialrating': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# use wrapt to patch django.views.View to call self.setup() if it exists
@wrapt.patch_function_wrapper(django.views.View, 'dispatch')
def view_dispatch_setup_wrapper(wrapped, instance, args, kwargs):
    if hasattr(instance, 'setup'):
        instance.setup(*args, **kwargs)
    return wrapped(*args, **kwargs)

