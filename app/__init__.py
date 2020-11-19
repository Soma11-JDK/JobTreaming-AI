from flask import Flask
from flask_cors import CORS
from app import SimilarityAnalyzer

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
analyzer = SimilarityAnalyzer.SimilarityAnalyzer()

from app.routes import *
