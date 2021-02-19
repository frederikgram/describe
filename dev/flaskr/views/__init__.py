""" """

import flask

from flask import Flask, render_template, url_for, request, current_app
from flaskr import app, controller, models


@app.route("/", methods=["GET", "POST"])
def index():
    """See comments
    on GET/POST branchings
    found in the code
    """

    # On GET request, we return a
    # template representing our image gallery
    # if a search query / similarity threshold
    # is given, pass those on to
    # controllers.build_image_gallery_view()
    if flask.request.method == "GET":

        current_app.logger.info("Attempting to fetch an image gallery view")

        query = request.form.get("search_query")
        threshold = request.form.get("search_threshold")

        return controller.build_image_gallery_view(query, threshold)

    # On POST, we except a JSON body
    # containing a base64 encoded image
    # and optionally, pre-defined
    # metadata related to the image
    if flask.request.method == "POST":
        pass


@app.route("/image/<image_path>", methods=["GET", "POST"])
def image_details(image_path: str):
    """Returns a template containing
    a more detailed view of a single
    given image from its image_path.

    Expected to be a local function,
    and not called by an end-user
    """

    current_app.logger.info("Attempting to fetch an image data view")
    return controller.build_image_data_view(image_path)
