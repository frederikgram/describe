""" """

import flask

from flask import Flask, render_template, url_for, request, current_app
from flaskr import app, models, controllers


@app.route("/", methods=["GET"])
def index():
    """See comments
    on GET/POST branchings
    found in the code
    """

    # On GET request, we return a
    # template representing our image gallery
    # if a search query / similarity threshold
    # is given, pass those on to
    # controllerss.build_image_gallery_view()
    if flask.request.method == "GET":

        current_app.logger.info("Attempting to fetch an image gallery view")
        query = request.form.get("search_query") or ""
        threshold = request.form.get("search_threshold")
        threshold = int(threshold) if threshold else 50
        current_app.logger.info(f"Received the query values of:\nquery: '{query}'\nthreshold: {threshold}")

        return controllers.build_image_gallery_view(query, threshold)

@app.route("/image/<image_path>", methods=["GET"])
def image_details(image_path: str):
    """Returns a template containing
    a more detailed view of a single
    given image from its image_path.

    Expected to be a local function,
    and not called by an end-user
    """

    current_app.logger.info("Attempting to fetch an image data view")
    return controllers.build_image_data_view(image_path)
