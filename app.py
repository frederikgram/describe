""" """
import os
import sys
import json
import time
import random
from werkzeug.utils import secure_filename
from typing import Dict, Iterator, Callable, Union, List
from flask import Flask, request, render_template, url_for, flash, redirect
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
app.secret_key = 'not_secret'
app.config['UPLOAD_FOLDER'] = "static/images"

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

metadata_db = json.load(open("static/metadata_db.json", 'r'))["images"]
example_queries = open("static/example_queries", 'r').read().split('\n')

SIMILARITY_THRESHOLD = 0.35
MAX_IMAGES = 100


def query_similarity(query_sentence: str, image_caption: str) -> float:
    """ compute the pairwise sentence similarity of two
        given sentences, using a matrix of TF-IDF features.  
    """

    corpus = [query_sentence, image_caption]                                                                                                                                                                                                 
    vect = TfidfVectorizer(min_df=1, stop_words="english")                                                                                                                                                                                                   
    tfidf = vect.fit_transform(corpus)                                                                                                                                                                                                                       
    pairwise_similarity = tfidf * tfidf.T 

    return pairwise_similarity.toarray()[0][1]

def segment_query(query_string: str) -> Dict[str, Callable]:
    """ Convert a descriptive english sentence
        into {str, Callable} token pairs,
        removing non-descriptive features.
    """

    return dict()

def filter_images(query_string: str = None) ->  Iterator[str]:
    """ Filter images based on the pairwise similarity
        between the user-given search query, and the
        image-caption created by the show-and-tell
        deep-learning model.
    """
    
    # yield only images that are semantically
    # similar to the given search query, and
    # within the globally defined threshold.
    for image, metadata in metadata_db.items():
        similarity = query_similarity(query_string, metadata['image_caption'])
        if similarity > SIMILARITY_THRESHOLD:
            yield (image, similarity)

def update_metadata(key: str, value: str):
    """ update metadata_db and dump to disk """

    # Put value
    metadata_db[key] = value

    # Save to disk
    json.dump(
        {"images": metadata_db},
        open("static/metadata_db.json", 'w')
    )

@app.route("/")
def index():
    """ Retrieves the search query from 
        the input form, and then pushes
        the query through our pipeline.
        
        Afterwards, we populate our webpage,
        with the data we collected in the
        previous stages.
    """
    
    search_query = request.args.get('query')

    if search_query:
        images = [img[0] for img in sorted(filter_images(search_query), key=lambda elem: elem[1])][:MAX_IMAGES]
    else:
        images = list(metadata_db.keys())[:MAX_IMAGES]

    image_info = []
    for image in images:
        image_info.append(
            (
                url_for('static', filename='images/') + image,
                metadata_db[image]["image_caption"]
            )
        )

    return render_template(
        template_name_or_list = "index.html",
        total_images = len(metadata_db.keys()),
        images = image_info,
        query_value = search_query if search_query else None,
        example_query = "Example: " + random.choice(example_queries)
    )


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

        update_metadata(filename, {"image_caption": get_caption(model, f"static/images/{filename}")})
        sys.stdout.write(f"{filename} was succesfully stored to disk, with the caption: {metadata_db[filename]['image_caption']}")
        flash(f"{filename} was succesfully stored to disk, with the caption: {metadata_db[filename]['image_caption']}")
    
if __name__ == "__main__":

    # Start Tensorflow Image-Captioning service
    #sys.path.append("./show_and_tell/")
    #from show_and_tell.main import start_model, get_caption

    #model = start_model()

    # Looks for new images since last startup,
    # if any, gather and append metadata to
    # their entries in metadata_db.json
    for filename in os.listdir("static/images"):
        continue
        # File does not have an entry
        if filename not in metadata_db:

            # Collect Metadata
            image_metadata = {"image_caption": get_caption(model, f"static/images/{filename}")}

            # Update and dump metadata
            # do this for every image, instead of dumping
            # once, as to not loss data on a program crash
            update_metadata(filename, image_metadata)
        
    app.run()
