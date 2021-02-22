""" """

from flask import current_app
from .actions import *
from flaskr.models.database_updaters import insert_new_images_into_db

def run_startup_procedures():
    """ Using the configuration file bound to
    the current flask application, run startup
    procedures concerning analysis and database
    management
    """

    current_app.logger.info("Running startup procedures as specified in the application config")

    if current_app.config["INSERT_NEW_IMAGES_ON_STARTUP"]:                                  
        insert_new_images_into_db()                                                 
    if current_app.config["ANALYZE_UNANALYSED_IMAGES_ON_STARTUP"]:                          
        analyse_all_unanalysed_images() 
