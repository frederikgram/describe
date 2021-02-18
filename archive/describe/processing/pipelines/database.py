""" """


from typing import List
from pony.orm import *

from describe.database import ImageDBEntity

@db_session
def fetch_all_images_from_db() -> List[ImageDBEntity]:
    """ """
    return list(select(img for img in ImageDBEntity))