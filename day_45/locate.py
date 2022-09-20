# GeoPy is one of the many fantastic Python library to get location of places and to find distance between two cities or countries. It can calculate distance between and two points if latitude and longitude of both points are known.GeoPy offers many more features to explore and to play with.

# We are using Nominatim class of geocoders sub-module from geopy to find location(latitude , longitude) of two places. Geodesic is being used to find the distance bewteen these two places.
from geopy.distance import geodesic as GD
from geopy.geocoders import Nominatim 

city1 = input('Enter first city name :')
city2 = input('Enter second city name :')
geolocator = Nominatim(user_agent='MyApp')

location_city1 = geolocator.geocode(city1)
location_city2 = geolocator.geocode(city2)

lat_long_city1 = (location_city1.latitude ,location_city1.longitude)
lat_long_city2 = (location_city2.latitude ,location_city2.longitude)

distance = GD(lat_long_city1 , lat_long_city2).km

print(f'The distance between {city1} and {city2} is { distance} km')