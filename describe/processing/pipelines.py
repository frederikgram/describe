""" """
import os
import json
import subprocess

from typing import Tuple, Dict, List
from pony.orm import *
from flask import url_for

from describe.database import ImageDBEntity

from describe.processing.captions import generate_caption
from describe.processing.objects import detect_objects


# Database Interaction
@db_session
def fetch_all_images_from_db() -> List[ImageDBEntity]:
    """ """
    return list(select(img for img in ImageDBEntity))

# Analysis Abstractions 
def get_metadata(filename: str) -> Tuple[str, str, List]:
    """ """

    path_to_images = "describe/static/images/"
    filename = filename

    caption = generate_caption(
        os.path.join(path_to_images, filename)
    )

    objects = detect_objects(
        os.path.join(path_to_images, filename)
    )

    return filename, caption, objects


# Startup Checks
@db_session
def on_startup():
    """ """

    print("Running Startup Procedures...")
 
    ## Add new Images
    print("Adding new images")
    path_to_images = "describe/static/images/"
    for filename in os.listdir(path_to_images):

        if filename[-4:] != ".jpg":
            continue

        # Remove extension
        filename = filename[:-4]

        try:
            ImageDBEntity[filename]
        except:
            _, caption, objects = get_metadata(filename + ".jpg")


            imgDBEnt = ImageDBEntity(
                filename = filename,
                caption = caption,
                objects = objects
            )

            print(f"Added new Image: {imgDBEnt}")

    commit()
