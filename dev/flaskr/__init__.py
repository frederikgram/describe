""" """
from flask import Flask
import os


def create_flask_app():
    app = Flask(__name__)
    return app


app = create_flask_app()

# Configure application logger
from .logging import configure_logger
configure_logger()

# Apply configurations
# to the Flask instance
# @TODO get config from an object in ./configs/ instead of from a static settings file
app.config.from_json("./configs/settings.json")
app.app_context().push()

# Setup Database interactions
from .models import init_app
init_app(app)

# Startup Procedures
from .controllers import run_startup_procedures
run_startup_procedures()

# Expose routes to end-user
from .views import *
