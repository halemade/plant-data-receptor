from flask import Flask
from flask_restful import Api, Resource

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, world!'


@server.route('/readings/<datetime>/<primary_sensor_id>/<reading_value>', methods=['POST'])
def return_data(datetime, primary_sensor_id, reading_value):
    return {'datetime':datetime, "id": primary_sensor_id, "reading_value":reading_value}

# app = Flask(__name__)
# api = Api(server)

# class SensorReading(Resource):
#     def post(self, datetime, primary_sensor_id, reading_value):
#         self.reading_value = reading_value
#         self.datetime = datetime
#         self.primary_sensor_id = primary_sensor_id
#         return {'datetime':self.datetime, "id": self.primary_sensor_id, "reading_value": self.reading_value}

# api.add_resource(SensorReading, "/readings/<string:datetime>/<string:primary_sensor_id>/<float:reading_value>")    

if __name__ == '__main__':
    server.run(debug=True, host="0.0.0.0", port=8050)
