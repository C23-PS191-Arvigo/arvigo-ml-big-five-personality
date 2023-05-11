from flask import Flask, request
import tensorflow as tf
import base64
import joblib
import numpy as np

def load_image_from_base64(base64_string, target_size=(100, 100)):
    img_bytes = base64.b64decode(base64_string)
    img = tf.io.decode_image(img_bytes, channels=3)
    img = tf.image.resize(img, target_size)
    img = img / 255.0
    img = tf.expand_dims(img, axis=0)
    return img

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def predict_image(model, img):
    # Adjust this function based on the specific requirements of your joblib model
    pred = model.predict(img)
    return pred  # It's an array within array, hence we need to extract it

def classify_face_shape(value):
    shapes = ['circle', 'heart', 'oblong', 'oval', 'square', 'triangle']
    probabilities = value.tolist()

    # Get the sorted probabilities array that would sort the probabilities in descending order
    sorted_probabilities_array = np.argsort(probabilities)[::-1]

    # Get the highest and second highest probabilities
    highest_probability = probabilities[sorted_probabilities_array[0]]
    second_highest_probability = probabilities[sorted_probabilities_array[1]]

    # Get the corresponding shapes using the sorted probabilities array
    highest_shape = shapes[sorted_probabilities_array[0]]
    second_highest_shape = shapes[sorted_probabilities_array[1]]

    return {
        'shape': highest_shape,
        'probability': highest_probability,
        'second_shape': second_highest_shape,
        'second_probability': second_highest_probability
    }


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Blank</p>"

@app.route('/face_shape', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.get_json()
        if json_data:
            # param = json_data['image']
        # return json_data

            argument = {'EXT1': 4, 'EXT2': 2, 'EXT3': 5, 'EXT4': 4, 'EXT5': 4, 'EXT6': 4, 'EXT7': 1, 'EXT8': 5, 'EXT9': 2, 'EXT10': 4, 'EST1': 1, 'EST2': 2, 'EST3': 3, 'EST4': 4, 'EST5': 3, 'EST6': 2, 'EST7': 1, 'EST8': 3, 'EST9': 3, 'EST10': 1, 'AGR1': 2, 'AGR2': 1, 'AGR3': 1, 'AGR4': 2, 'AGR5': 3, 'AGR6': 5, 'AGR7': 1, 'AGR8': 1, 'AGR9': 5, 'AGR10': 5, 'CSN1': 3, 'CSN2': 1, 'CSN3': 1, 'CSN4': 5, 'CSN5': 4, 'CSN6': 2, 'CSN7': 4, 'CSN8': 2, 'CSN9': 2, 'CSN10': 2, 'OPN1': 2, 'OPN2': 4, 'OPN3': 2, 'OPN4': 3, 'OPN5': 5, 'OPN6': 5, 'OPN7': 4, 'OPN8': 5, 'OPN9': 4, 'OPN10': 2}
            # model = load_model("./model_kmeans.joblib")  # Update the file extension
            model = joblib.load("./model_kmeans.joblib")  # Update the file extension
            pred = model.predict(argument)
            return str(pred)
            # img = load_image_from_base64(param)
            pred = predict_image(model, argument)
            # result = classify_face_shape(pred)

            return str(pred)
        else:
            return 'Image data not found in the JSON payload.'
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    app.run()
