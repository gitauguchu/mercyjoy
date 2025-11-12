import sys, os
from pathlib import Path

# Path to your project directory
BASE_DIR = Path(__file__).resolve().parent

# Add project path to system path
sys.path.insert(0, str(BASE_DIR))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'mercyjoy_events.settings'  # <-- change this!

# Import Django WSGI app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
