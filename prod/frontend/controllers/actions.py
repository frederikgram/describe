""" """

import os
import base64
import requests
import flask

from flask import current_app
from frontend import models
from typing import *


def fetch_database_statistics() -> Dict[str, Any]:
    """Fetches various information about the
    data stored in the database.

    Examples of this could be the number of
    unanalysed images vs. the number of
    analysed images.
    """

    current_app.logger.info("Attempting to fetch database statistics")

    total_number_of_images = len(models.get_all_images())
    number_of_analysed_images = len(models.get_all_analysed_images())
    number_of_unanalysed_images = len(models.get_all_unanalysed_images())

    return {
        "num_images": total_number_of_images,
        "num_analysed_images": number_of_analysed_images,
        "num_unanalysed_images": number_of_unanalysed_images,
    }


def fetch_all_analysed_images() -> List[Dict[str, any]]:
    """Requests a list of dictionaries
    representing all the analysed images currently
    available in our image database
    """

    current_app.logger.info("Attempting to fetch all analysed images")

    analysed_images = models.get_all_analysed_images()
    return analysed_images


def fetch_all_unanalysed_images() -> List[Dict[str, any]]:
    """Requests a list of dictionaries
    representing all the unanalysed images currently
    available in our image database
    """

    current_app.logger.info("Attempting to fetch all unanalysed images")

    analysed_images = models.get_all_analysed_images()
    return analysed_images


def analyse_all_unanalysed_images():
    """Initializes the analysis
    pipeline for all images in the
    database that haven't been
    analysed yet"""

    current_app.logger.info(
        "Attempting to initialize analysis of all unanalysed images"
    )
    unanalysed_images = models.get_all_unanalysed_images()


def analyze_image_from_path(image_path: str) -> Dict[str, Any]:
    """Given an image path, this function will
    encode that image to base64, and make an
    API request to the pipeline service found under
        describe/services/pipeline
    and returns a dictionary with the
    format as seen in the
        describe/services/pipeline/
    API spefication
    """

    current_app.logger.info(f"Attempting to analyse an image from path: '{image_path}'")

    image_as_base_64 = _convert_image_path_to_base64_object(image_path)

    # @TODO insert a dynamic way of getting api endpoints for external services
    return dict()


def _convert_image_from_path_to_base64_object(image_path: str) -> bytes:
    """Attempts to create the base64 representation
    of the image in the image_path location
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Path: '{image_path}' does not exist")

    current_app.logger.info(
        f"Attempting to conver the image at path: '{image_path}' to a base64 object"
    )
    with open(image_path, "rb") as image_file:
        try:
            data = base64.b64encode(image_file.read())
        except Exception as e:
            raise e

    return data
