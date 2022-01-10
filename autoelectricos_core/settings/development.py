

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5#yfmvus%tbifzd)eub-&%r9_-pld7-sfh%)8j$+%#$l7o=b5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
import dj_database_url
import os
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}