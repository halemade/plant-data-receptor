import requests

BASE = "https://dash-customer-success.plotly.host/plant-data-receptor/"

sensor_endpoint = "/readings"
datetime = "20220502T01:01:00"
sensor_id = "sensor_id_string"
reading_value =3.26

payload = {'csrf_token': 'dEjS0pYL6yq8CnMieQQ3p2s3VDR5hWWX', 'has_password': True, 'username': 'taylor','is_active': True}

session = requests.Session()
session.auth = ('taylor', 'dataliberation')

auth = session.post(BASE)
# response = requests.post(BASE+f"readings/{datetime}/{sensor_id}/{reading_value}")
response = requests.post(BASE+f"readings/{datetime}", auth=('taylor','dataliberation'))

if response.status_code != 200:
    print(response.status_code)
else:
    print(response.json())
