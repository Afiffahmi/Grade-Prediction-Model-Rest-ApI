from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, request
import numpy as np
import pickle
from flask_cors import CORS


APP = Flask(__name__)
CORS(APP)
API = Api(APP)

 ##loading the model from the saved file
pkl_filename = "knn_model.pkl"
with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)


class Predict(Resource):
    @staticmethod
    def post():
        data = request.get_json(force=True)  # Get data from POST request

        predictions = []
        for entry in data:
                # Extract student ID from entry
            student_id = entry.pop('student_id', None)
            X_new = np.fromiter(entry.values(), dtype=float)  # convert input to array

            # Predict for each entry
            prediction_value = model.predict([X_new])[0]

            # Map prediction value to grade
            grade = map_prediction_to_grade(prediction_value)

            predictions.append({'Student ID': student_id,'Input': entry, 'Prediction': grade,'predictionvalue': prediction_value})  # Include input data in response

        return {'Predictions': predictions}, 200

def map_prediction_to_grade(prediction):
        if 2.3 <= prediction < 2.7:
            return 'F'
        elif 2.7 <= prediction < 3.0:
            return 'C+'
        elif 3.0 <= prediction < 3.1:
            return 'B-'
        elif 3.1 <= prediction < 3.4:
            return 'B'
        elif 3.4 <= prediction < 3.5:
            return 'B+'
        elif 3.5 <= prediction < 3.55:
            return 'A-'
        elif 3.55 <= prediction < 3.7:
            return 'A'
        elif 3.7 <= prediction:
            return 'A+'
        

 @APP.route('/')
def index():
    return "Hello, World!"    


API.add_resource(Predict, '/predict')




if __name__ == '__main__':
    APP.run(debug=True, port='1080')