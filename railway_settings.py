"""
Railway-specific Django settings
"""
import os

def update_django_settings():
    """Update Django settings for Railway deployment"""
    
    # Import Django settings
    from django.conf import settings
    
    # Update ALLOWED_HOSTS for Railway
    railway_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', '')
    
    if railway_domain:
        # Add the Railway domain
        if railway_domain not in settings.ALLOWED_HOSTS:
            settings.ALLOWED_HOSTS.append(railway_domain)
        
        # Also add the base domain without any port
        base_domain = railway_domain.split(':')[0]
        if base_domain not in settings.ALLOWED_HOSTS:
            settings.ALLOWED_HOSTS.append(base_domain)
    
    # For immediate fix, allow all (remove this in production)
    print(f"Railway Domain: {railway_domain}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    return settings

# Call the function to update settings
update_django_settings()