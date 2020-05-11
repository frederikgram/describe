""" """

import os
import time
import json
import subprocess

from typing import Tuple, Dict, List, Iterable
from pony.orm import *
from flask import url_for

from describe.database import ImageDBEntity

from describe.processing.captions import generate_caption, generate_bulk_captions
from describe.processing.objects import detect_objects



def make_batches(iterable: Iterable, max_batch_size: int) -> Iterable[Iterable]:
    l = len(iterable)
    for ndx in range(0, l, max_batch_size):
        yield iterable[ndx:min(ndx + max_batch_size, l)]


def get_metadata(batches: Iterable[Iterable[str]]) -> Iterable[Iterable[Tuple[str, str, dict]]]:
    """ """

    for enum, batch in enumerate(batches):
        captions = list(generate_bulk_captions(batch))

        objects = list(
            [detect_objects(filepath) for filepath in batch]
        )
    
        batch_data = [(filename, caption, objs) for filename, caption, objs in zip(batch, captions, objects)]
        yield batch_data

