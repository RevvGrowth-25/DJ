import os
from django.core.wsgi import get_wsgi_application
from io import BytesIO
from urllib.parse import unquote

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Revv.settings")

application = get_wsgi_application()

def handler(event, context):
    """Minimal WSGI adapter for Vercel."""
    environ = {
        "REQUEST_METHOD": event["method"],
        "PATH_INFO": unquote(event["path"]),
        "QUERY_STRING": event.get("queryString", ""),
        "SERVER_NAME": "vercel.app",
        "SERVER_PORT": "80",
        "wsgi.input": BytesIO(event.get("body", "").encode("utf-8")),
        "wsgi.errors": BytesIO(),
        "wsgi.version": (1, 0),
        "wsgi.run_once": False,
        "wsgi.url_scheme": "https",
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
    }

    # Set headers
    for header, value in event.get("headers", {}).items():
        environ[f"HTTP_{header.upper().replace('-', '_')}"] = value

    response = []

    def start_response(status, headers):
        response.append(status)
        response.append(headers)

    body = b"".join(application(environ, start_response))
    status = int(response[0].split()[0])

    headers_dict = {k: v for k, v in response[1]}

    return {
        "statusCode": status,
        "headers": headers_dict,
        "body": body.decode("utf-8"),
    }
