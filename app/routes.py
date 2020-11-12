from flask import request, jsonify
import requests as requests
from app import app, analyzer
import json

LECTURE_URL = "http://117.16.136.156:8085/lecture/listAll"
PETITION_URL = "http://117.16.136.156:8085/petition/add"


@app.route('/recommend', methods=['GET'])
def recommend():
    query = request.values.get('query')
    response = requests.get(url=LECTURE_URL).text

    lectures = json.loads(response)
    r_lectures = []
    for l in lectures:
        similarity = analyzer.cosine_sim(l['title'], query)
        print(similarity)
        if similarity >= 0.3:
            l['similarity'] = similarity
            r_lectures.append(l)

    if len(r_lectures) <= 0:
        token = request.headers.get('Authorization')
        if token is not None:
            payload = {'title': query, 'contents': query}
            headers = {'Authorization': request.headers.get('Authorization'), 'Content-Type': 'application/json'}
            requests.post(url=PETITION_URL, data=json.dumps(payload), headers=headers)
            '''
            headers = {'Authorization': 'Bearer ' + 'eyJyZWdEYXRlIjoxNjA1MTcxMjI3NTA0LCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiUk9MRV9FWFBFUlQiLCJleHAiOjE2MDc3NjMyMjcsImVtYWlsIjoidGVzdEB0ZXN0LnRlc3QifQ.LDpGVIYATDNB3F-ApQxAuIILcQ8bAs5jPG0UCWI5RO0',
                   'Content-Type': 'application/json'}
            '''
    else:
        r_lectures = sorted(r_lectures, key=lambda lecture: lecture['similarity'], reverse=True)

    return jsonify(r_lectures)
