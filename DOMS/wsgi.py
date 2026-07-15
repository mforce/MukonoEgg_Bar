"""
WSGI config for DOMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DOMS.settings")

application = get_wsgi_application()

# NOTE: The old `from whitenoise.django import DjangoWhiteNoise` wrapper used
# here was removed in whitenoise 4.x. Static-file serving is now handled by
# WhiteNoiseMiddleware (see DOMS/settings.py MIDDLEWARE), which is the
# supported way to integrate whitenoise into a Django WSGI app.