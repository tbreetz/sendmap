import csv
import requests
import re
import sqlite3
import time
import sys

def tick_import(file):
    #Parse ticks CSV
    print(file)
    with open(file) as f:
        data = {}
        freader = csv.reader(f, delimiter=',')
        for row in freader:
            data[row[1]] = [row[4], row[6]]

    coords = {}
    location_links = {data[x][1]:data[x][0] for x in data.keys()}
    del location_links["Location"]

    #connect to DB
    conn = sqlite3.connect('./db.sqlite3')
    c = conn.cursor()

    #download pages for routes at new crags, get geolocation
    print(f'{len(location_links.keys())} unique crags')
    new_crags = 0
    for l in location_links.keys():
        modL = l.replace("'","''")
        exists = c.execute(f"SELECT * FROM app_crag WHERE name = '{modL}'")
        exists = exists.fetchone()
        if exists is not None: 
            print(exists)
        else:
            res = requests.get(location_links[l])
            lats = re.finditer('latitude": "([-\d]\d+\.\d*)', res.text)
            lons = re.finditer('longitude": "([-\d]\d+\.\d*)', res.text)
            for lat in lats:
                craglat = lat.group(1)
            for lon in lons :
                craglon = lon.group(1)
            coords[l] = (craglat, craglon)
            print(l)
            new_crags += 1
            #sleep to limit download rate
            time.sleep(2)

    count = c.execute("SELECT * FROM app_crag ORDER BY id DESC LIMIT 1")
    count = count.fetchone()[0]
    for i, crag in enumerate(coords.keys()):
        lat = coords[crag][0]
        lon = coords[crag][1]
        c.execute('insert into app_crag values (?,?,?,?)', (count + i + 1, crag, lat, lon))

    conn.commit()

    print(f'{len(location_links.keys())} unique crags')
    print(f'{new_crags} crags imported')
