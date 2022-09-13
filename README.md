# plant-data-receptor
Flask api for posting ioT readings
This is the code I use to create the Flask api, also hosted on DE.
QtPy_code.py contains the code that I run on the microcontroller that posts the readings to the Flask api.
This api writes to one of the onboard Postgres dbs and the Dash app reads from it.
