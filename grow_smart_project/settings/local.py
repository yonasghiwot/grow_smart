"""
This module contains local settings for the Grow Smart project.
"""
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grow_smart_gui',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': '3306',
    }
}
