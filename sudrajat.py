from flask import Flask, request, jsonify
import joblib
import traceback
import numpy as np
import random

app = Flask(__name__)

# Load the joblib model
model = joblib.load("model_kmeans.joblib")  # Update the path to your joblib model file

@app.route("/detect_personality", methods=["POST"])
def detect_personality():
    if request.content_type == "application/json":
        try:
            # data = request.get_json()
            data = {'EXT1': 4, 'EXT2': 2, 'EXT3': 5, 'EXT4': 4, 'EXT5': 4, 'EXT6': 4, 'EXT7': 1, 'EXT8': 5, 'EXT9': 2, 'EXT10': 4, 'EST1': 1, 'EST2': 2, 'EST3': 3, 'EST4': 4, 'EST5': 3, 'EST6': 2, 'EST7': 1, 'EST8': 3, 'EST9': 3, 'EST10': 1, 'AGR1': 2, 'AGR2': 1, 'AGR3': 1, 'AGR4': 2, 'AGR5': 3, 'AGR6': 5, 'AGR7': 1, 'AGR8': 1, 'AGR9': 5, 'AGR10': 5, 'CSN1': 3, 'CSN2': 1, 'CSN3': 1, 'CSN4': 5, 'CSN5': 4, 'CSN6': 2, 'CSN7': 4, 'CSN8': 2, 'CSN9': 2, 'CSN10': 2, 'OPN1': 2, 'OPN2': 4, 'OPN3': 2, 'OPN4': 3, 'OPN5': 5, 'OPN6': 5, 'OPN7': 4, 'OPN8': 5, 'OPN9': 4, 'OPN10': 2}
            # data = {'EXT1': 5, 'EXT2': 2, 'EXT3': 1, 'EXT4': 1, 'EXT5': 4, 'EXT6': 4, 'EXT7': 5, 'EXT8': 5, 'EXT9': 3, 'EXT10': 4, 'EST1': 3, 'EST2': 3, 'EST3': 5, 'EST4': 3, 'EST5': 5, 'EST6': 1, 'EST7': 5, 'EST8': 4, 'EST9': 1, 'EST10': 3, 'AGR1': 5, 'AGR2': 4, 'AGR3': 2, 'AGR4': 4, 'AGR5': 3, 'AGR6': 3, 'AGR7': 4, 'AGR8': 2, 'AGR9': 1, 'AGR10': 5, 'CSN1': 2, 'CSN2': 2, 'CSN3': 4, 'CSN4': 4, 'CSN5': 1, 'CSN6': 1, 'CSN7': 2, 'CSN8': 2, 'CSN9': 3, 'CSN10': 2, 'OPN1': 1, 'OPN2': 1, 'OPN3': 5, 'OPN4': 2, 'OPN5': 1, 'OPN6': 3, 'OPN7': 4, 'OPN8': 2, 'OPN9': 1, 'OPN10': 3}
            # sample_data = {
#     'EXT1': 4, 'EXT2': 2, 'EXT3': 5, 'EXT4': 4, 'EXT5': 4, 'EXT6': 4, 'EXT7': 1, 'EXT8': 5, 'EXT9': 2, 'EXT10': 4,
#     'EST1': 1, 'EST2': 2, 'EST3': 3, 'EST4': 4, 'EST5': 3, 'EST6': 2, 'EST7': 1, 'EST8': 3, 'EST9': 3, 'EST10': 1,
#     'AGR1': 2, 'AGR2': 1, 'AGR3': 1, 'AGR4': 2, 'AGR5': 3, 'AGR6': 5, 'AGR7': 1, 'AGR8': 1, 'AGR9': 5, 'AGR10': 5,
#     'CSN1': 3, 'CSN2': 1, 'CSN3': 1, 'CSN4': 5, 'CSN5': 4, 'CSN6': 2, 'CSN7': 4, 'CSN8': 2, 'CSN9': 2, 'CSN10': 2,
#     'OPN1': 2, 'OPN2': 4, 'OPN3': 2, 'OPN4': 3, 'OPN5': 5, 'OPN6': 5, 'OPN7': 4, 'OPN8': 5, 'OPN9': 4, 'OPN10': 2
# }

# Randomize each value in the dictionary
            # data = {key: random.randint(1, 5) for key in sample_data}
            # Perform any necessary preprocessing on the input data
            # ...
            # Convert the dictionary into a list
            input_data = np.array(list(data.values())).reshape(1, -1)


            # Make predictions using the loaded joblib model
            predictions = model.predict(input_data)  # Assuming the model expects a list of inputs

            # Process the predictions and prepare the output
            # ...

            # Return the output as a JSON response
            # return jsonify({"predictions": predictions.tolist()})
            return str(predictions)

        except Exception as e:
            error_message = str(e)
            traceback_info = traceback.format_exc()
            return jsonify({"error": error_message, "traceback": traceback_info}), 500

    else:
        return jsonify({"error": "Invalid content-type. Expected application/json."}), 400

if __name__ == "__main__":
    app.run()
