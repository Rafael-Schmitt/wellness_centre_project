#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import urllib.parse

def fix_database_url():
    """Fix DATABASE_URL for psycopg2"""
    if 'DATABASE_URL' in os.environ:
        db_url = os.environ['DATABASE_URL']
        # Convert postgres:// to postgresql://
        if db_url.startswith('postgres://'):
            os.environ['DATABASE_URL'] = db_url.replace('postgres://', 'postgresql://', 1)

def main():
    """Run administrative tasks."""
    # Fix database URL before Django loads
    fix_database_url()
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wellness_centre.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()