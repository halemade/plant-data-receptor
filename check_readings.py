from models import RealReadings, Plants
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
import datetime
import os
from sqlalchemy import create_engine
from multiprocessing.util import register_after_fork

def dispose_engine(engine):
 # dispose SqlAlchemy engine in register_after_fork
    engine.dispose()

connection_string = "postgresql+psycopg2" + os.environ.get(
    "DATABASE_URL"
).lstrip("postgres")
engine = create_engine(connection_string)

register_after_fork(engine, dispose_engine)

Session = sessionmaker(bind=engine)
session = Session()
# num_readings = [p.plant_name for p in session.query(Plants)]
# plants table is good

# time = datetime.datetime.now()
# adjusted_for_timezone = time - datetime.timedelta(hours=4)
# reading = {"id": '2001', "reading_value":1000, "time":adjusted_for_timezone.strftime(format="%Y-%m-%d %H:%M:%S")}
# new_reading = RealReadings(
#         datetime = reading["time"],
#         reading_value = reading["reading_value"],
#         primary_sensor_id = reading["id"]
#     )
# breakpoint()
# session.add(new_reading)
# session.commit()

num_readings = session.query(RealReadings).count()
print(num_readings)
session.close
