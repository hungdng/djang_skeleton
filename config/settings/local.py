# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Add Django Debug Toolbar
"""

import os
from .base import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
# https://stackoverflow.com/questions/29455057/django-core-exceptions-improperlyconfigured-the-secret-key-setting-must-not-be
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='f!@165#^)y6ajk)-gk9w@cx=ccz)e*qyt8cctd64(f&5=)tvi0')

ALLOWED_HOSTS = ["*"]

# CORS header settings
# ------------------------------------------------------------------------------

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    # 'example.com', # your domain
    'localhost:3000',
    '127.0.0.1:3000',
    'localhost:8000',
    '127.0.0.1:8000',
)
# CORS_ALLOW_CREDENTIALS = True

from core.logger import LOGGING

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', 'localhost']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
