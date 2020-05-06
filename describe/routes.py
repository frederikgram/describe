""" """
import random

from flask import render_template, url_for, request

from describe import app
from describe.processing import pipelines

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dev")
def dev():

    images = pipelines.fetch_all_images_from_db()
    search_query = request.args.get('query')

    return render_template(
        "index.html",
        total_images = len(images),
        images = [(
            # Path to Image
            url_for("static", filename="images/") + img.filename + ".jpg",
            # Pretty formatted caption
            f'"{img.caption}"' if img.caption != "" else "No Caption Generated",
            # Pretty formatted objects
            "No Objects Detected" if len(img.objects) == 0 else [f"{list(obj.keys())[0]}, certainty: {round(list(obj.values())[0] * 100, 2)}%" for obj in img.objects])
            for img in images],
        query_value = search_query if search_query else None,
    )