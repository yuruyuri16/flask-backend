from flask import Flask, render_template
import face_recognition
import cv2
import rtree

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
