import requests

for i in range(1,61):
    star=requests.get(f"https://swapi.dev/api/planets/{i}/")
    planet=star.json()
    print(planet['name'])
