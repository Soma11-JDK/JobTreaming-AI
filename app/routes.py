from flask import request, jsonify
import requests as requests
from app import app, analyzer
import json

URL = "http://117.16.136.156:8085/lecture/listAll"


@app.route('/recommend', methods=['GET'])
def recommend():
    query = request.values.get('query')
    # params = {'query': query}
    # response = requests.get(url=URL, params=params).text
    response = requests.get(url=URL).text

    lectures = json.loads(response)

    for l in lectures:
        l['similarity'] = analyzer.cosine_sim(l['title'], query)

    lectures = sorted(lectures, key=lambda lecture: lecture['similarity'], reverse=True)
    return jsonify(lectures)
