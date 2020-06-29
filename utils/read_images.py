import os
import face_recognition
import pickle

IMAGES_DIR = '../data/'

faces = dict()

filename = '../data.bin'
# file = open(filename, 'wb')
#
# count = 1
# for person_dir in os.listdir(IMAGES_DIR):
#     faces[person_dir] = []
#     print(count, '/', len(os.listdir(IMAGES_DIR)))
#     for image_file in os.listdir(IMAGES_DIR + person_dir):
#         image = face_recognition.load_image_file(IMAGES_DIR + person_dir + '/' + image_file)
#         face_encoding = face_recognition.face_encodings(image)
#         if (len(face_encoding) != 0):
#             face_encoding = face_encoding[0]
#             faces[person_dir].append(face_encoding)
#     count += 1
#
# pickle.dump(faces, file)
#
# file.close()

# file = open(filename, 'rb')
# faces_obj = pickle.load(file)
# for k, v in faces_obj.items():
#     for encoding in v:
#         print(encoding)


# read other data dirs

dirs = ["data104", "data212", "data343", "data420", "data529", "data650"]

for dir in dirs:
    faces = {}
    file = open('../' + dir + '.bin', 'wb')
    print(dir)
    for person_dir in os.listdir('../' + dir):
        faces[person_dir] = []
        for image_file in os.listdir('../' + dir + '/' + person_dir):
            image = face_recognition.load_image_file('../' + dir + '/'+ person_dir + '/' + image_file)
            face_encoding = face_recognition.face_encodings(image)
            if (len(face_encoding) != 0):
                face_encoding = face_encoding[0]
                faces[person_dir].append(face_encoding)
    pickle.dump(faces, file)

for dir in dirs:
    file = open('../' + dir + '.bin', 'rb')
    obj = pickle.load(file)
    for k, v in obj.items():
        for encoding in v:
            print(encoding)
    print()