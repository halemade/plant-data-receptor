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
    "DATABASE_URL", "postgres://postgres:docker@127.0.0.1:5436"
).lstrip("postgres")
engine = create_engine(connection_string)

register_after_fork(engine, dispose_engine)


Base = declarative_base()

class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer)
    plant_name = Column(String)
    common_name = Column(String)
    zone = Column(String)
    size = Column(String)
    x = Column(Integer)
    y = Column(Integer)
    src = Column(String)
    water_low = Column(BigInteger)
    water_high = Column(String)

    def __repr__(self):
        return f"<Comment(\n\tname='{self.zd_id}'\n\tsubject='{self.subject}'\n)>"

class Readings(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    reading_value = Column(Float)
    primary_sensor_id = Column(Integer)

    def __repr__(self):
        return f"<Reading(\n\ttype='{self.reading_type}'\n\treading value='{self.reading_value}'\n)>"


class Sensors(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    zone = Column(Integer)
    sensor_id = Column(String)

    def __repr__(self):
        return f"<Sensor(\n\tname='{self.sensor_id}'\n\tsubject='{self.subject}'\n)>"

# create all the tables
Base.metadata.create_all(engine)