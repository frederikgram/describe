""" """

import os
import base64

import requests

import flask
from flask import render_template, url_for, redirect

from typing import *

from flaskr import models

def build_image_gallery(query: str):
    """ Acts as the pipeline for 
    all of the controller behavior.
    
    Returns the ../templates/gallery.html template
    with all its attributes filled in
    """

    images = models.get_unanalyzed_images()
    print(images)
    return render_template("gallery.html", images=images)

def build_image_data_view(image_path: str):
    """ """
    image = models.get_image_from_image_path(image_path)
    return render_template("image_data_view.html", image=image)

def fetch_database_statistics() -> Dict[str, Any]:
    """ Fetches various information about the
    data stored in the database.
    
    Examples of this could be the number of
    unanalyzed images vs. the number of
    analyzed images.
    """

    # @TODO fetch some nice stats
    return dict()


def fetch_all_analyzed_images() -> List[Dict[str, any]]:
    """ Requests a list of dictionaries
    representing all the analyzed images currently
    available in our image database
    """

    analyzed_images = models.get_analyzed_images()
    return analyzed_images


def analyze_image_from_path(path_to_image: str) -> Dict[str, Any]:
    """ Given an image path, this function will
    encode that image to base64, and make an
    API request to the pipeline service found under
        describe/services/pipeline
    and returns a dictionary with the
    format as seen in the 
        describe/services/pipeline/ 
    API spefication
    """

    image_as_base_64 = _convert_image_path_to_base64_object(path_to_image)

    # @TODO insert a dynamic way of getting api endpoints for external services
    return dict()


def _convert_image_from_path_to_base64_object(image_path: str) -> bytes:
    """ Attempts to create the base64 representation
        of the image in the image_path location
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Path: '{image_path}' does not exist")

    with open(image_path, "rb") as image_file:
        try:
            data = base64.b64encode(image_file.read())
        except Exception as e:
            raise e

    return data

