from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
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
        parser = reqparse.RequestParser()
        parser.add_argument('test1')
        parser.add_argument('test2')
        parser.add_argument('assignment1')
        parser.add_argument('assignment2')
        parser.add_argument('quiz1')
        parser.add_argument('carrymark')


        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': model.predict([X_new])[0]}

        if 0 <= out['Prediction'] < 0.5:
            out['Prediction'] = 'F' 
        elif 0.5 <= out['Prediction'] < 1.5:
            out['Prediction'] = 'D' 
        elif 1.5 <= out['Prediction'] < 2.5:
            out['Prediction'] = 'D'
        elif 2.5 <= out['Prediction'] < 3.5:
            out['Prediction'] = 'B'
        elif 3.5 <= out['Prediction'] < 4.5:
            out['Prediction'] = 'B'
        elif 4.5 <= out['Prediction'] < 5:
            out['Prediction'] = 'A'


        return ({'Prediction': out}), 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':

    APP.run(debug=True, port='1080')