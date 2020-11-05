

<img src="./demos/banner.png" alt="drawing"/>
:bookmark: [Fast forward to the model evaluations](./models.md)

:bookmark: [Fast forward to the interactive demo](#)


# About

Search images by describing their appearance using
conversational language. Without lemmatization supporting for in-image objects imilarity and word2vec encodings.

No pre-made metadata required! Everything is 
analyzed and stored _on-the-fly_.

# How does it work?
Every image added to the ```./static/images/``` folder is analysed using a pipeline of:
- Object Detection (YOLOv3)
- Caption Generation (CNN -> RNN)

When the user is searching, we perform the
following process on the input query.
- Query Processing (Tokenizing, Word2Vec etc.)
- Similarity Analysis
  - TFIDF Similaity (Query and Caption),
  - Object-by-Object Similarity (between the query and the objects detected in the stored images. # Word2Vec Encoded) 

After this, we can get an ensemble prediction using the weighted mean of object certainties\
combined with the TFIDF Similarity result for how well the caption matches the given search query.

## Links
[My Website](https://frederikgram.github.io/) and 
[My LinkedIn](https://www.linkedin.com/in/frederikgramkortegaard/).
## Running the service
Currently, the service is not in a state where it can easily be deployed. A complete docker-solution is in development. A demo of the searching process can be seen [here](./demos/search_demo.gif) (the visual metadata is in this case, purely placeholder).  
For a preview of how the metadata actually looks for each image can be seen [here](./demos/metadata_showcase.gif) (the GUI is purely for showcase purposes and does not reflect any real product design).
