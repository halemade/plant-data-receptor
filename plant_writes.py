import pandas as pd
from models import Plants, Sensors, engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

plant_df = pd.read_csv('plants_table_write.csv')

Session = sessionmaker(bind=engine)
session = Session()


#read in plants dataframe

for plant in plant_df.iterrows():
    new_plant = Plants(
        # id = plant[0],
        sensor_id = plant[1]['network_alias_id'],
        plant_name = plant[1]['plant_name'],
        common_name = plant[1]['common_name'],
        zone = plant[1]['zone'],
        size = plant[1]['size'],
        x = plant[1]['x'],
        y =plant[1]['y'],
        src = plant[1]['src'],
        water_low = plant[1]['water_low'],
        water_high = plant[1]['water_high'],
    )
    print(type(new_plant))
    session.add(new_plant)

try:
    session.commit()
except Error as e:
    print(e)
    session.rollback()

session.close