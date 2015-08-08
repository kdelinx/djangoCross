import os, sys
from django.core.wsgi import get_wsgi_application

path = os.path.dirname(os.path.dirname(__file__))
if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoCross.settings'

application = get_wsgi_application()
