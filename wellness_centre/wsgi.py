import os
from django.core.wsgi import get_wsgi_application

# Apply Railway settings before loading Django
try:
    from dj_database_url import config as db_config
    DATABASES = {
        'default': db_config(default=os.environ.get('DATABASE_URL'))
    }   
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wellness_centre.settings')

application = get_wsgi_application()