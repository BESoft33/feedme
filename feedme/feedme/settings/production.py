from .base import *
from . import config

SECRET_KEY = config.SECRET_KEY
KHALTI_SECRET_KEY = config.KHALTI_SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
]