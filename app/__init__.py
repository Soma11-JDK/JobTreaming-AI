from flask import Flask
from app import SimilarityAnalyzer

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
analyzer = SimilarityAnalyzer.SimilarityAnalyzer()

from app.routes import *