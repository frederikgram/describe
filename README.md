

<img src="./demos/banner.png" alt="drawing"/>

# About

Search images by describing their appearance using
conversational Language, supporting both context
_and_ object similarity.

No pre-made metadata required! everything is 
analyzed and stored _on-the-fly_.

# How does it work?
Every image added to the ```./static/images/``` folder is analysed using a pipeline of:
- Object Detection (YOLOv3)
- Caption Generation (CNN -> RNN)
- Query Processing (Tokenizing, Word2Vec etc.)
- Similarity Analysis
  - TFID Similaity (Query and Caption),
  - Object-by-Object Similarity (Word2Vec Encoded) 

After this, we can get an ensemble prediction using the Weighted Mean of gitObject Certainties combined with the TFIDSimilarity result using a weighted dot-function.

## Links
[My Website](https://frederikgram.github.io/) and 
[My LinkedIn](https://www.linkedin.com/in/frederikgramkortegaard/).
## Running the service
Currently, the service is not in a state where it can easily be deployed. A complete docker-solution is in development.