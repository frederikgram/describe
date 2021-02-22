""" """

import os
import pickle
import codecs
import sqlite3

from typing import *
from flask import current_app, g, jsonify
from .database_management import get_db


def update_image_metadata_from_image_path(image_path: str, metadata: Dict):
    """ """

    pickled = codecs.encode(pickle.dumps(metadata), "base64").decode()
    db = get_db()
    cur = db.cursor()
    cur.execute(
        f'UPDATE images SET metadata = "{pickled}" WHERE path = "{image_path}" AND metadata IS NULL'
    )

    db.commit()


def insert_new_images_into_db():
    """Looks for files in the static images folder
    and tries to insert them into the image database.

    Ignores both images that already exist in the database
    and images whose file-extension is not supported
    as described in
        ../describe/frontend/settings.json"""

    path_to_images = current_app.config["PATH_TO_IMAGES"]
    if not os.path.exists(path_to_images):
        raise FileNotFoundError(f"Path: '{path_to_images}' could not be found")

    allowed_extensions = current_app.config["ACCEPTED_IMAGE_FILE_TYPES"]
    db = get_db()
    cur = db.cursor()
    for image_path in os.listdir(path_to_images):
        if image_path.split(".")[1] not in allowed_extensions:
            continue
        cur.execute(f'INSERT OR IGNORE INTO images (path) VALUES ("{image_path}")')
    db.commit()