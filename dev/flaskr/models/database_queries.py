""" """

import sqlite3
import pickle
import codecs
from typing import *

from flask import current_app, g
from .database_management import get_db


def get_unanalyzed_images() -> List[str]:
    """ """
    cur = get_db().cursor()
    cur.execute("SELECT * FROM images WHERE metadata IS NULL")
    rows = cur.fetchall()
        

    return [dict(row) for row in rows]


def get_analyzed_images():
    """ """
    cur = get_db().cursor()
    cur.execute("SELECT * FROM images WHERE metadata IS NOT NULL")
    rows = cur.fetchall()


    return []

def get_image_from_image_path(image_path: str):
    """ """
    cur = get_db().cursor()
    cur.execute(f'SELECT path FROM images WHERE path = "{image_path}"')
    rows = cur.fetchall()
    return dict(rows[0])