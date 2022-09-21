import requests

star=requests.get("https://swapi.dev/api/planets/")
planet=star.json()
# for plan in planet['name']:
#     print(plan)
print(planet.values())