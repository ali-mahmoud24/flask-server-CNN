from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from CNN.model import show_info



app = Flask(__name__)
CORS(app)



UPLOAD_FOLDER = '/uploads'  # Define the upload folder path
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def hello():
    return 'Hello, this is your Flask API!'


# CNN

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    if file:
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(file_path)

      name, info, questions = show_info(file_path)
      return jsonify({'name': name, 'info': info, 'questions': questions})



# # SENTIEMENT ANALYSIS

# # Send data as json { "review": ['text..............'] }
# @app.route('/predict', methods=['POST'])
# def predict_review():

#   review = request.json['review']

#   rating = predict_sentimnet(review)

#   return jsonify({'rating': rating})



if __name__ == '__main__':
    app.run(debug=True)