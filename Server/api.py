from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import ast
from data import getTestData

app = Flask(__name__)
api = Api(app)

#Methods for test class
class Test(Resource):
    def get(self):
        data = getTestData().to_dict()
        return {"data": data}, 200    
    pass

#/test is the endpoint
api.add_resource(Test, "/test")

if __name__ == '__main__':
    app.run()  # run our Flask app