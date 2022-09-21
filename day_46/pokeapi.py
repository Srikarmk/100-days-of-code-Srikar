import requests

pokeName=input("Enter the name of the pokemon\t").lower()

poke=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokeName}')
data=poke.json()

for type in data['types']:
    pokeType=type['type']['name']
    print(f"{pokeName.upper()} is of {pokeType.upper()} type")

print('\t')
weight=data['weight']
print(f"{pokeName} weight is {weight} kg")

print('\t')
print(f"{pokeName.upper()}'s ATTACKS")
for ability in data['abilities']:
    print(ability['ability']['name'])
    
print('\t')
print(f"{pokeName.upper()}'s STATS")
for stat in data['stats']:
    baseStat=stat['base_stat']
    statName=stat['stat']['name']
    print(f'{statName} -> {baseStat}')