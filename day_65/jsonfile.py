import json
from textwrap import indent

with open("P:/Python/Projects/names.json","r") as d:
    data=json.load(d)
    # data['like']="Movies"
    # new_data=json.dump(data,indent=4)

print(data)