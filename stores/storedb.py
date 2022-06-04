import json
from datetime import datetime
from pathlib import Path
import psycopg2

DATA_FILENAME = 'data/andorra-data.json'
CITY = 'Andorra'

def load_data():
    conn = psycopg2.connect(
    host="localhost",
    database="delivery-plat", 
    user="postgres", 
    password="15255796")

    cur = conn.cursor()
    id = 0

    jsonfile = Path(__file__).parents[1] / DATA_FILENAME
    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    id += 1
                    name = tags.get('name','N/A')

                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = f'POINT({longitude} {latitude})'

                    housenumber = tags.get('addr:housenumber', 'N/A')
                    street = tags.get('addr:street', 'N/A')
                    postcode = tags.get('addr:postcode', 'N/A')
                    address = housenumber + ',' + street + ',' + postcode

                    store_type = tags.get('shop', 'N/A')
                    phone = tags.get('phone', 'N/A')

                    cur.execute("""INSERT INTO stores_store 
                    (id,
                    created_at, 
                    name, 
                    rating,
                    longitude, 
                    latitude, 
                    location, 
                    address, 
                    store_type,
                    opening_hour,
                    closing_hour,
                    phone, 
                    city) 
                    VALUES (%(id)s,
                    %(created_at)s, 
                    %(name)s, 
                    %(rating)s,
                    %(longitude)s, 
                    %(latitude)s, 
                    %(location)s,
                    %(address)s, 
                    %(store_type)s,
                    %(opening_hour)s,
                    %(closing_hour)s,
                    %(phone)s, 
                    %(city)s)""", 
                    {'id': id,
                    'created_at': datetime.now(),
                    'name': name,
                    'rating': 0.0,
                    'longitude': longitude,
                    'latitude': latitude,
                    'location': location,
                    'address': address,
                    'store_type': store_type,
                    'opening_hour': None,
                    'closing_hour': None,
                    'phone': phone,
                    'city': CITY})
            except KeyError:
                pass
    conn.commit()

    cur.close()
    conn.close()


if __name__ == '__main__':
    load_data()
