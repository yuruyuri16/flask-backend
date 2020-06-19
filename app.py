from flask import Flask, render_template, request, flash, redirect, url_for
import face_recognition
import cv2
import rtree
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


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    error = None
    if request.method == 'POST':
        print(request.form)
        print(request.url)
        print(dict(request.files))
        if 'image' not in request.files:
            flash('No input with the image name')
            return redirect(request.url)
        file = request.files['image']

        if file.filename == '':
            error = 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Successful submission')
            return redirect(url_for('upload'))
    return render_template('upload.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
