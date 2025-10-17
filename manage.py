#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.wsgi import get_wsgi_application  # ✅ add this

# ✅ This line lets Vercel use this file as a WSGI entry point
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Revv.settings')
app = get_wsgi_application()  # 👈 this exposes 'app' for Vercel

def main():
    """Run administrative tasks."""
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
