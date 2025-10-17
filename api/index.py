import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Match this to your Django project folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Revv.settings')

application = get_wsgi_application()

# For Vercel's serverless function
def handler(event, context):
    from io import BytesIO
    from urllib.parse import unquote

    environ = {
        'REQUEST_METHOD': event.get('method', 'GET'),
        'PATH_INFO': unquote(event.get('path', '/')),
        'QUERY_STRING': event.get('queryString', ''),
        'SERVER_NAME': 'vercel.app',
        'SERVER_PORT': '80',
        'wsgi.input': BytesIO(event.get('body', '').encode('utf-8')),
        'wsgi.errors': BytesIO(),
        'wsgi.version': (1, 0),
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'https',
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
    }

    for k, v in event.get('headers', {}).items():
        environ[f'HTTP_{k.upper().replace("-", "_")}'] = v

    response = []
    def start_response(status, headers):
        response.append(status)
        response.append(headers)

    body = b''.join(application(environ, start_response))
    status = int(response[0].split()[0])
    headers_dict = {k: v for k, v in response[1]}

    return {
        'statusCode': status,
        'headers': headers_dict,
        'body': body.decode('utf-8', errors='ignore'),
    }
