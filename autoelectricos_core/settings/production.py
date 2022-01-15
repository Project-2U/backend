from .base import *




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
