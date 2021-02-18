""" """

from pony.orm import *
db = Database()

class ImageDBEntity(db.Entity):
    filename = PrimaryKey(str)
    caption = Optional(str)
    objects = Optional(Json)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
print("Database Loaded")