from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [
    'https://autoelectricos-store.herokuapp.com/'
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}