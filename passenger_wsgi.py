import os
import sys
from mercyjoy_events.wsgi import application

# Path to your project directory
BASE_DIR = Path(__file__).resolve().parent

# Add project path to system path
sys.path.insert(0, str(BASE_DIR))
