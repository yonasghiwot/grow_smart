from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grow_smart_gui',
        'USER': 'root',
        'PASSWORD':'grow_smart',
        'HOST':'localhost',
        'PORT': '3306',
    }
}
