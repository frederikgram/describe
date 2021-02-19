""" """
from flask import Flask
import logging
from logging.config import dictConfig
import os

# Setup logging configuration
logging.getLogger("werkzeug").setLevel(logging.ERROR)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
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


def create_flask_app():
    app = Flask(__name__)
    return app


app = create_flask_app()

# Apply configurations
# to the Flask instance
app.config.from_json("settings.json")
app.app_context().push()

# Configure Logger
app.logger.level

# Setup working directory for
# consistency of file management


# Setup Database interactions
from .models import init_app, insert_new_images_into_db

init_app(app)

if app.config["INSERT_NEW_IMAGES_ON_STARTUP"]:
    insert_new_images_into_db()

from .controller import analyse_all_unanalysed_images

if app.config["ANALYZE_UNANALYSED_IMAGES_ON_STARTUP"]:
    analyse_all_unanalysed_images()

# Expose routes to end-user
from .views import *
