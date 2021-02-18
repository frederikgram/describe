""" """
from flask import url_for

from .database_management import *
from .database_queries import *
from .database_updaters import *

insert_new_images_into_db("./flaskr/static/images")