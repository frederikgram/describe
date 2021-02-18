""" """

import flask
from flask import Flask, render_template, url_for, request
from flaskr import app, controller, models

@app.route('/', methods=["GET", "POST"])
def index():
    """ """

    if flask.request.method == "GET":
        query = request.form.get("search_query", None)
        return controller.build_image_gallery(query)

    if flask.request.method == "POST":
        pass

@app.route('/image/<image_path>', methods=["GET", "POST"])
def image_details(image_path: str):
    """ """
    print(image_path)
    print("trying to build an image data view")
    return controller.build_image_data_view(image_path)