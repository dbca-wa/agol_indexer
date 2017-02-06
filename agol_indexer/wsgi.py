"""
WSGI config for agol_indexer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import confy
import os

from django.core.wsgi import get_wsgi_application

confy.read_environment_file('.env')  # Must precede dj_static imports.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agol_indexer.settings")

application = get_wsgi_application()
