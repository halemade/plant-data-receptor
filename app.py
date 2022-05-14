from flask import Flask
from flask_restful import Api, Resource

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, world!'


@server.route('/readings/<primary_sensor_id>/<reading_value>', methods=['POST'])
def return_data(primary_sensor_id, reading_value):
    reading = {"id": primary_sensor_id, "reading_value":reading_value} 
    print(reading)
    return reading

if __name__ == '__main__':
    server.run(debug=True, host="0.0.0.0", port=8050)
