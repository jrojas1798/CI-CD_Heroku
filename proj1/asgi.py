"""
ASGI config for proj1 project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj1.settings')

application = get_asgi_application()
