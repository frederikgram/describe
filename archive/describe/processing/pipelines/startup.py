""" """
import os
import time
import math
import json
import subprocess

from typing import Tuple, Dict, List
from pony.orm import *
from flask import url_for

from tqdm import tqdm

from describe.database import ImageDBEntity

from describe.processing.pipelines.analysis import make_batches, get_metadata
from describe.processing.pipelines.database import fetch_all_images_from_db

# Tensorflow model for caption generation
# has to be reloaded every batch, so
# set this to the max
# your pc can handle
MAX_IMAGE_BATCH_SIZE = 5

@db_session
def add_new_images():
    """ """

    ## Check for new images
    images_to_add = list()
    path_to_images = "describe/static/images/"

    for filename in os.listdir(path_to_images):

        if filename[-4:] != ".jpg":
            continue
        try:
            ImageDBEntity[filename[:-4]]
        except:
            images_to_add.append(filename)
            print(f"Found new image, added {filename} to analysis queue")

    ## Analyze new images in batches
    if len(images_to_add) != 0:
        print(f"Starting Metadata Analysis on {len(images_to_add)} images")
    
        batches = make_batches(
            [os.path.join(path_to_images, filename) for filename in images_to_add],
            MAX_IMAGE_BATCH_SIZE
        )

        print(f"Converted {len(images_to_add)} images to {math.ceil(len(images_to_add) / MAX_IMAGE_BATCH_SIZE)} batches of size {MAX_IMAGE_BATCH_SIZE}")

        total_diffs = {}

        for enum, batch_outputs in enumerate(get_metadata(batches)):

            print(f"Analyzing batch {enum}")
            t1 = time.time()
            # Map Metadata lists to their
            # filenames and add to database
            for filename, caption, objs in batch_outputs:
                filename = filename[len(path_to_images):-4]
                print(f"Adding {filename} to database with metadata")
                ImageDBEntity(
                    filename = filename,
                    caption = caption,
                    objects = objs   
            )

            t2 = time.time()
            t_diff = t2 - t1

            print(f"""Batch {enum} containing {len(batch_outputs)} images took {t_diff} seconds to analyze and add to database.
                which is {t_diff / len(batch_outputs)} seconds pr images on average""")

            total_diffs[enum] = t_diff

            print("Commiting changes")
            commit()
        
        print(f"Average time pr batch: {sum(total_diffs.values()) / len(total_diffs)} seconds")

@db_session
def remove_unavailable_entries():

    ## Removing DB entries whose image is not available
    path_to_images = "describe/static/images/"

    for dbEntity in fetch_all_images_from_db():
        if dbEntity.filename + ".jpg" not in os.listdir(path_to_images):
            print(f'Deleting entry: "{dbEntity.filename}.jpg" ...')
            dbEntity.delete()

    print("commiting changes")
    commit()


# Startup Checks
@db_session
def on_startup():
    """ """
    print("Running Startup Procedures...")
    
    print("Cleaning DB Entries whose images are unavailable")
    remove_unavailable_entries()

    print("Searching for new images")
    add_new_images()
