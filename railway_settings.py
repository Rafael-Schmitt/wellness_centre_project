import os

# Railway-specific database settings
def get_railway_db_config():
    if 'DATABASE_URL' not in os.environ:
        return None
    
    db_url = os.environ['DATABASE_URL']
    
    # Parse the URL
    from urllib.parse import urlparse
    result = urlparse(db_url)
    
    config = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': result.path[1:],
        'USER': result.username,
        'PASSWORD': result.password,
        'HOST': result.hostname,
        'PORT': result.port,
        'CONN_MAX_AGE': 600,
    }
    
    # Handle SSL - use connection string approach
    query_params = {}
    if result.query:
        from urllib.parse import parse_qs
        query_params = parse_qs(result.query)
    
    # Build connection string without sslmode in Django config
    # Let psycopg2 handle it through the URL
    return config

# Update settings
import wellness_centre.settings as settings

db_config = get_railway_db_config()
if db_config:
    settings.DATABASES['default'] = db_config