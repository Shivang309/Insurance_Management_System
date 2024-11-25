"""
WSGI config for Insurance_Management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Insurance_Management.settings')

application = get_wsgi_application()
app = application

'''
import os
from django.core.wsgi import get_wsgi_application

# If you are using WhiteNoise in production, you'll need this line
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Insurance_Management.settings')

application = get_wsgi_application()

# Add WhiteNoise to serve static files (in production)
application = WhiteNoise(application)
'''