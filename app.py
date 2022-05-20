from flask import Flask
from flask_restful import Api, Resource
import datetime

from models import engine, RealReadings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

Session = sessionmaker(bind=engine)
session = Session()

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, world!'


@server.route('/readings/<primary_sensor_id>/<reading_value>', methods=['POST'])
def return_data(primary_sensor_id, reading_value):
    session = Session()
    time = datetime.datetime.now()
    adjusted_for_timezone = time - datetime.timedelta(hours=4)
    reading = {"id": str(primary_sensor_id), "reading_value":int(reading_value), "time":adjusted_for_timezone.strftime(format="%Y-%m-%d %H:%M:%S")}
    new_reading = RealReadings(
        datetime = reading["time"],
        reading_value = reading["reading_value"],
        primary_sensor_id = reading["id"]
    )
    session.add(new_reading)

    try:
        session.commit()
    except Error as e:
        print(e)
        session.rollback()
    session.close()
    print(reading)
    return reading

if __name__ == '__main__':
    server.run(debug=True, host="0.0.0.0", port=8050)
