import requests

workspace_base = "http://172.17.0.67:8050"
deployed_base = ""

sensor_endpoint = "/readings"
datetime = "20220502T01:01:00"
sensor_id = "sensor_id_string"
reading_value =3.26


session = requests.Session()
session.auth = ('taylor', 'dataliberation')

auth = session.post(BASE)
response = requests.post(workspace_base+f"/readings/{datetime}/{sensor_id}/{reading_value}")


if response.status_code != 200:
    print(response.status_code)
else:
    print(response.json())
