from flask import Flask, request
from flask_cors import cross_origin
import face_recognition
import cv2
from rtree import index
import os
from werkzeug.utils import secure_filename

WORKING_DIRECTORY = os.getcwd()
UPLOAD_FOLDER = WORKING_DIRECTORY + '/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    if request.method == 'POST':
        file = request.files['image']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            face_image = face_recognition.load_image_file(UPLOAD_FOLDER + file.filename)
            encoding = face_recognition.face_encodings(face_image)
            data = {
                'response': 'Enviado con exito.'
            }
            return data, 200


if __name__ == '__main__':
    app.run(debug=True)
