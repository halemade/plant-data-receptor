from models import engine, RealReadings, Plants
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
import datetime

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

num_readings = [p.reading_value for p in session.query(RealReadings)]
print(len(num_readings))
session.close
