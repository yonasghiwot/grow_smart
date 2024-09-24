from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grow_smart_db',
        'USER': 'grow_smart_user',
        'PASSWORD':'Phil_6613!',
        'HOST':'localhost',
        'PORT': '3306',
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'" 
        }
    }

}