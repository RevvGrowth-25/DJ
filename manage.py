#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Revv.settings')

app = get_wsgi_application()  # 👈 Add this line (Vercel looks for 'app')

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
