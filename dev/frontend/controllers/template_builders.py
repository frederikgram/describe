""" Builds templates found in 
    ../static/templates/
    by fetching relevant data
    from the following scripts 
        ./actions.py
        ../models/
    """

import os
import base64
import requests
import flask

from typing import *
from flask import render_template, url_for, redirect, current_app
from typing import *
from frontend import models


def build_image_gallery_view(query: str, similarity_treshhold: int):
    """Acts as the pipeline for
    all of the controller behavior.

    Returns the ../static/templates/gallery.html template
    with all its attributes filled in
    """

    current_app.logger.info("Attempting to build an image gallery")

    # @TODO  This is where we would call some
    # analytics stuff, to match query and similarity
    # with the analysed images in the db
    images = models.get_all_unanalysed_images()
    return render_template("image_gallery_view.html", images=images)


def build_image_data_view(image_path: str):
    """Acts as the pipeline for
    building a template with
    specific details for a given image.

    Returns the ../static/templates/image_data_view.html template
    with all its attributes filled in
    """

    current_app.logger.info("Attempting to build an image data view")

    image = models.get_image_from_image_path(image_path)
    return render_template("image_data_view.html", image=image)
