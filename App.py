from flask import Flask
from flask_restful import Api, Resource, reqparse
import numpy as np
import pickle

APP = Flask(__name__)
API = Api(APP)

 ##loading the model from the saved file
pkl_filename = "model.pkl"
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
        parser.add_argument('taking_notes')
        parser.add_argument('attendance')
        parser.add_argument('listening')

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': model.predict([X_new])[0]}

        if out['Prediction'] >= 1 and out['Prediction'] < 2:
            out['Prediction'] = 'D F' 
        elif out['Prediction'] >= 2 and out['Prediction'] < 3:
            out['Prediction'] = 'C D'
        elif out['Prediction'] >= 3 and out['Prediction'] < 4:
            out['Prediction'] = 'B C'
        elif out['Prediction'] >= 4 and out['Prediction'] < 5:
            out['Prediction'] = 'A B'
        elif out['Prediction'] == 5:
            out['Prediction'] = 'A'

        return out['Prediction'], 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')