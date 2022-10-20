import json 


str='''
{
    "name":"Srikar",
    "age":20,
    "isStudent":true,
    "skills":["python","c","blender"]
}
'''

data=json.loads(str)  #to load json data s means string
data['likes']="Anime"

new_data=json.dumps(data,indent=4,sort_keys=True) #to load data to json s means string
print(new_data)