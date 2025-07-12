import json
import os

def get_fav_num():
    filename = 'data.json'
    if (os.path.getsize(filename) > 0):
        with open(filename) as f:
            fav_num = json.load(f)
        return fav_num
    else:
        return None
