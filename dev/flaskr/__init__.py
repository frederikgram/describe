""" """
import sys
sys.dont_write_bytecode = True

from flask import Flask
app = Flask(__name__)
app.config.from_json("settings.json")
app.app_context().push()
from .models import init_app, get_db, update_image_metadata_from_image_path
init_app(app)
from .views import *


update_image_metadata_from_image_path("3.jpg", {1:"test"})