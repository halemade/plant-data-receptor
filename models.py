from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Computed, Integer, BigInteger,Boolean, String, DateTime, Float, ForeignKey, UniqueConstraint, Text, Index, desc
import os

import sqlalchemy as sa

from multiprocessing.util import register_after_fork

def dispose_engine(engine):
 # dispose SqlAlchemy engine in register_after_fork
    engine.dispose()

connection_string = "postgresql+psycopg2" + os.environ.get(
    "DATABASE_URL").lstrip("postgres")
engine = create_engine(connection_string)

register_after_fork(engine, dispose_engine)


Base = declarative_base()

class Plants(Base):
    __tablename__ = 'plants'

    sensor_id = Column(Integer, primary_key=True)
    plant_name = Column(String)
    common_name = Column(String)
    zone = Column(Integer)
    size = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)
    src = Column(String)
    water_low = Column(BigInteger)
    water_high = Column(BigInteger)

    def __repr__(self):
        return f"< Plant Record(\n\tplant_name='{self.plant_name}'\n\tzone='{self.zone}'\n)>"

class Readings(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    reading_value = Column(Float)
    primary_sensor_id = Column(Integer)

    def __repr__(self):
        return f"<Reading(\n\ttype='{self.primary_sensor_id}'\n\treading value='{self.reading_value}'\n)>"

class RealReadings(Base):
    __tablename__ = 'realreadings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    reading_value = Column(Float)
    primary_sensor_id = Column(Integer)

    def __repr__(self):
        return f"<RealReading(\n\ttype='{self.primary_sensor_id}'\n\treading value='{self.reading_value}'\n)>"


class Sensors(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    network_alias = Column(Integer)
    i2c_address = Column(String)
    sensor_type = Column(String)
    location_name = Column(String)
    zone = Column(Integer)

    def __repr__(self):
        return f"<Sensor(\n\tname='{self.sensor_id}'\n\tsubject='{self.subject}'\n)>"

# create all the tables
# Base.metadata.create_all(engine)