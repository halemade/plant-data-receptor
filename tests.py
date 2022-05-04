import requests

BASE = "https://dash-customer-success.plotly.host/plant-data-receptor/"

sensor_endpoint = "/readings"
datetime = "20220502T01:01:00"
sensor_id = "sensor_id_string"
reading_value =3.26

# response = requests.post(BASE+f"readings/{datetime}/{sensor_id}/{reading_value}")
response = requests.post(BASE+f"readings/{datetime}")

print(response.json())
