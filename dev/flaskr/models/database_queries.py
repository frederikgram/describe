""" """

import sqlite3
import pickle
import codecs

from typing import *
from flask import current_app, g
from .database_management import get_db


def _convert_row_to_dict(row) -> Dict[str, Any]:
    """Currently we naively convert
    an sqlite3 row into a dict
    """

    return dict(row)


def get_all_unanalysed_images() -> List[str]:
    """ """

    current_app.logger.info("Attempting to get all unanalysed images")
    cur = get_db().cursor()
    cur.execute("SELECT * FROM images WHERE metadata IS NULL")
    rows = cur.fetchall()

    return [dict(row) for row in rows]


def get_all_analysed_images():
    """ """
    current_app.logger.info("Attempting to get all analysed images")
    cur = get_db().cursor()
    cur.execute("SELECT * FROM images WHERE metadata IS NOT NULL")
    rows = cur.fetchall()

    return [_convert_row_to_dict(row) for row in rows]


def get_all_images():
    """ """
    current_app.logger.info("Attempting to get all images")
    cur = get_db().cursor()
    cur.execute("SELECT * FROM images")
    rows = cur.fetchall()

    return [_convert_row_to_dict(row) for row in rows]


def get_image_from_image_path(image_path: str):
    """ """
    current_app.logger.info(f"Attempting to get an image from path: '{image_path}'")
    cur = get_db().cursor()
    cur.execute(f'SELECT path FROM images WHERE path = "{image_path}"')
    rows = cur.fetchall()
    return dict(rows[0])
