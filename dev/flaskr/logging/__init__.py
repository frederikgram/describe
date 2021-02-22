""" Configure application logger """

import logging
from logging.config import dictConfig

def configure_logger():

    # Setup logging configuration
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    
    # Setup custom logging format using dictConfig

    dictConfig(
        {
         "version": 1,
         "formatters": {
             "default": {
                 "format": "[%(asctime)s] %(levelname)s in %(pathname)s::%(funcName)s: '%(message)s'",
             }
         },
         "handlers": {
             "wsgi": {
                 "class": "logging.StreamHandler",
                 "stream": "ext://flask.logging.wsgi_errors_stream",
                 "formatter": "default",
             }
         },
         "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )
