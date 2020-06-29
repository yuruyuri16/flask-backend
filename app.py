import json
from dataclasses import dataclass, field
from typing import Any
import pickle
import math
from flask import Flask, request, jsonify
from flask_cors import cross_origin
import face_recognition
from rtree import index
import os
from pathlib import Path
from werkzeug.utils import secure_filename
import numpy as np
from queue import PriorityQueue
import time

@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: Any=field(compare=False)


Path('static/images').mkdir(parents=True, exist_ok=True)

# Static variables
WORKING_DIRECTORY = os.getcwd()
UPLOAD_FOLDER = WORKING_DIRECTORY + '/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Flask app configs
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_face_encoding(image: np.array) -> np.array:
   face_encoding = face_recognition.face_encodings(image)
   if face_encoding == []:
       return []

   return face_encoding[0]


def read_encodings_file(r: str = '') -> []:
    file = open('data' + r + '.bin', 'rb')
    result = pickle.load(file)
    return result


all_encodings = read_encodings_file()
all_encodings104 = read_encodings_file('104')
all_encodings212 = read_encodings_file('212')
all_encodings343 = read_encodings_file('343')
all_encodings420 = read_encodings_file('420')
all_encodings529 = read_encodings_file('529')
all_encodings650 = read_encodings_file('650')


def ed(e1, e2):
    sum = 0
    for i in range(128):
        sum += math.pow((e1[i] - e2[i]), 2)
    return math.sqrt(sum)


def md(e1, e2):
    sum = 0
    for i in range(128):
        sum += abs(e1[i] - e2[i])
    return sum


def knn(query, k):
    queue = PriorityQueue()
    for person, encodings in all_encodings104.items():
        for encoding in encodings:
            dist = ed(query, encoding)
            queue.put(PrioritizedItem(dist, {person: dist}))
    return [queue.get() for i in range(k)]


def rtree(query, k):
    query = tuple(query)
    p = index.Property()
    d = {}

    p.dimension = 128
    idx128d = index.Index('128d_index104', properties=p)
    i = 0
    for person, encodings in all_encodings104.items():
        for encoding in encodings:
            d[i] = person
            t = tuple(encoding)
            t += t
            idx128d.insert(i, t)
            i += 1
    lres = list(idx128d.nearest(coordinates=query, num_results=k))
    return [d[i] for i in lres]


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    if request.method == 'POST':
        file = request.files['image']

        k = int(request.form['k'])

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            face_image = face_recognition.load_image_file(UPLOAD_FOLDER + file.filename)
            face_encoding = get_face_encoding(face_image)
            if face_encoding == []:
                return {
                    'message': 'no face detected'
                }, 422
            print(file.filename, k)
            start = time.time()
            k_list = knn(face_encoding, k)
            end = time.time()
            print('knn:', end - start)
            start = time.time()
            people = rtree(face_encoding, k)
            end = time.time()
            print('rtree:', end - start)
            data = {'knn': [], 'rtree': []}
            for result in k_list:
                for k, v in result.item.items():
                    data['knn'].append({k: v})
            data['rtree'] = people
            return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)
