from flask import Flask
from flask_restful import Api

from resources.sum import SumAPI

app = Flask(__name__)

api = Api(app, prefix='/api')
api.add_resource(SumAPI, '/add', endpoint="add", methods=["GET"])


@app.route('/')
def index():
   return "Addition App"


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
