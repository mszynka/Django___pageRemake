"""
WSGI config for thePage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/var/www/mszynka/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thePage.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
