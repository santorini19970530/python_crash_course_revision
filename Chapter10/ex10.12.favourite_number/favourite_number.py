# Python Crash Course, 2Ed, writtern by Eric Matthes

from read_data import get_fav_num
from write_data import record_fav_num

fav_num = get_fav_num()
if fav_num != None:
    print(f"I know your favourite number! it's {fav_num}.")
else:
    record_fav_num()
        
