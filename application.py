import logging
import logging.handlers
import subprocess
import time
import os

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
                response = web_header + photo_submission_body_start
                # saving the file received in data without checks for now
                filename = '/tmp/' + str(int(time.time() * 10000))
                f = open(filename, 'wb')
                f.write(environ['wsgi.input'].read(request_body_size))
                f.close()
                
                # calling exiftool withthat file
                exif_result = subprocess.run(['exiftool', filename], stdout=subprocess.PIPE)
                if exif_result.returncode == 0:
                    exif_result = str(exif_result.stdout)
                    for line in exif_result.split('\n'):
                        if 'gps' in line.lower():
                            response += line + html_newline
                    logger.info("Processed the image")
                else:
                    logger.error("Exiftool couldn't process image")
                    response += photo_submission_error
                os.remove(filename)
                response += photo_submission_body_end + page_end
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
