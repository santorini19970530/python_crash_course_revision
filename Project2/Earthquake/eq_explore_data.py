# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

# Explore the structure of the data.

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Generate readable json file
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags)
print(lons)
print(lats)
