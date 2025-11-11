import sys, os
sys.path.insert(0, '/home3/karibuke/repositories/mercyjoy1')

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
