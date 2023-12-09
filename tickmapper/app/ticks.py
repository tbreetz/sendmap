import csv
import requests
import re
import sqlite3
import time
import sys
from app import models

def tick_import(user, row):
    print('debug')
    user = models.profile.objects.get(userName=user)
    crag = models.crag.objects.get(name = row[6])
    models.tick.objects.create(user=user, date=row[0], name=row[1], route_type=row[11], height=row[13], grade=row[2], crag=crag)
    print(f'{user} added a tick')
    return


def crag_import(user, file):
    #Parse ticks CSV
    #print(file)
    profile = models.profile.objects.get(userName=user)
    with open(file) as f:
        data = {}
        freader = csv.reader(f, delimiter=',')
        unloaded_crags = []
        ticks_added = 0
        entries = []
        for i, row in enumerate(freader):
            data[row[1]] = [row[4], row[6]]
            if i != 0: #ignore header row
                try:
                    #print(row[6], user)
                    try:
                        crag = models.crag.objects.get(name = row[6])
                        ticks_added += 1
                    except:
                        #print(row[6], " not found")
                        unloaded_crags.append(row)
                        continue
                    if row[13] == '': height = 0 
                    else: height = row[13]
                    if row[2] == '': grade = 'N/A' 
                    else: grade = row[2]
                    #print(row, height, grade)
                    entries.append(models.tick(user=profile, date=row[0], name=row[1], route_type=row[11], height=height, grade=grade, crag=crag))
                except:
                    print('ERR: ' + row)

    #models.tick.objects.bulk_create(entries, ignore_conflicts=True)
    coords = {}
    location_links = {data[x][1]:data[x][0] for x in data.keys()}
    del location_links["Location"]
    #connect to DB
    conn = sqlite3.connect('./db.sqlite3')
    c = conn.cursor()
    #download pages for routes at new crags, get geolocation
    #print(f'{len(location_links.keys())} unique crags')
    new_crags = 0
    for l in location_links.keys():
        modL = l.replace("'","''")
        exists = c.execute(f"SELECT * FROM app_crag WHERE name = '{modL}'")
        exists = exists.fetchone()
        if exists is not None: 
            print(exists)
        else:
            if not l:
                continue
            print(l)
            res = requests.get(location_links[l])
            lats = re.finditer('latitude": "([-\d]\d+\.\d*)', res.text)
            lons = re.finditer('longitude": "([-\d]\d+\.\d*)', res.text)
            for lat in lats:
                craglat = lat.group(1)
            for lon in lons :
                craglon = lon.group(1)
            coords[l] = (craglat, craglon)
            new_crags += 1
            #sleep to limit download rate
            time.sleep(.5)
    #count = c.execute("SELECT * FROM app_crag ORDER BY id DESC LIMIT 1")
    #count = count.fetchone()[0]
    crag_entries = []
    for crag in coords.keys():
        #print('CRAG: ', crag)
        lat = float(coords[crag][0])
        lon = float(coords[crag][1])
        crag_entries.append(models.crag(name=crag, lat=lat, lon=lon))

    '''for i, crag in enumerate(coords.keys()):
        lat = coords[crag][0]
        lon = coords[crag][1]
        c.execute('insert into app_crag values (?,?,?,?)', (count + i + 1, crag, lat, lon))
    conn.commit()'''
    #print(len(crag_entries), crag_entries[:5])
    #print(len(entries), entries[:5])
    res = models.crag.objects.bulk_create(crag_entries, batch_size=500, ignore_conflicts=True)
    print('new crags :', len(res), ' ', new_crags)
    time.sleep(.2)
    res = models.tick.objects.bulk_create(entries, batch_size=500, ignore_conflicts=True)
    print('ticks 1:', len(res))
    unloaded_entries = []
    for row in unloaded_crags:
        if row[13] == '': height = 0 
        else: height = row[13]
        if row[2] == '': grade = 'N/A' 
        else: grade = row[2]
        #print(row[6])
        try:
            crag = models.crag.objects.get(name = row[6])
        except Exception as e:
            print('E: ',e)
        unloaded_entries.append(models.tick(user=profile, date=row[0], name=row[1], route_type=row[11], height=height, grade=grade, crag=crag))
    
    print(unloaded_entries[:3])
    time.sleep(.2)
    res = models.tick.objects.bulk_create(unloaded_entries, batch_size=500, ignore_conflicts=True)
    print('ticks 2:', len(res))
    ticks_added += len(unloaded_crags)
    data = {'unique': len(location_links.keys()),
            'new': new_crags,
            'ticks': ticks_added
            }
    print(data)
    return data



