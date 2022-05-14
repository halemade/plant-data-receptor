from flask import Flask
from flask_restful import Api, Resource
import datetime

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, world!'


@server.route('/readings/<primary_sensor_id>/<reading_value>', methods=['POST'])
def return_data(primary_sensor_id, reading_value):
    time = datetime.datetime.now()
    reading = {"id": primary_sensor_id, "reading_value":reading_value, "time":time.strftime(format="%Y-%m-%d %H:%M:%S")}
    time = datetime.datetime.now()
    print(reading)
    return reading

if __name__ == '__main__':
    server.run(debug=True, host="0.0.0.0", port=8050)
