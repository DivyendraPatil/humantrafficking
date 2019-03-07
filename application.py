import logging
import logging.handlers

from html_pages import *

from wsgiref.simple_server import make_server


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/opt/python/log/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)


def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    response = None
    
    if method == 'POST':
        try:
            request_body_size = int(environ['CONTENT_LENGTH'])
            if path == '/':
                request_body = environ['wsgi.input'].read(request_body_size).decode()
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
            elif path == '/check':
                logger.info("Received content of length: %d" % request_body_size)
                logger.info("Received content of type: %s" % environ['CONTENT_TYPE'])
                logger.info("Saved the image as req.jpg")
                f = open('/tmp/req.jpg', 'wb')
                f.write(environ['wsgi.input'].read(request_body_size))
                f.close()
                response = welcome
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        if not response:
            response = ''
    else:
        response = welcome

    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
