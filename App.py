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
            X_new = np.fromiter(entry.values(), dtype=float)  # convert input to array

            # Predict for each entry
            prediction_value = model.predict([X_new])[0]

            # Map prediction value to grade
            grade = map_prediction_to_grade(prediction_value)

            predictions.append({'Input': entry, 'Prediction': grade})  # Include input data in response

        return {'Predictions': predictions}, 200

def map_prediction_to_grade(prediction):
        if 0 <= prediction < 0.5:
            return 'F' 
        elif 0.5 <= prediction < 1.0:
            return 'F+' 
        elif 1.0 <= prediction < 1.3:
            return 'D-' 
        elif 1.3 <= prediction < 1.7:
            return 'D' 
        elif 1.7 <= prediction < 2.0:
            return 'D+' 
        elif 2.0 <= prediction < 2.3:
            return 'C-' 
        elif 2.3 <= prediction < 2.7:
            return 'C' 
        elif 2.7 <= prediction < 3.0:
            return 'C+' 
        elif 3.0 <= prediction < 3.3:
            return 'B-' 
        elif 3.3 <= prediction < 3.7:
            return 'B' 
        elif 3.7 <= prediction < 4.0:
            return 'B+' 
        elif 4.0 <= prediction < 4.3:
            return 'A-' 
        elif prediction >= 4.3:
            return 'A'

     


API.add_resource(Predict, '/predict')

if __name__ == '__main__':

    APP.run(debug=True, port='1080')