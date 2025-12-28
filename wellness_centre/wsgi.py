import os
from django.core.wsgi import get_wsgi_application

# Apply Railway settings before loading Django
try:
    from railway_settings import update_django_settings
    update_django_settings()
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wellness_centre.settings')

application = get_wsgi_application()