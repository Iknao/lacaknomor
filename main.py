import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))
from opencage.geocoder import OpenCageGeoCode
key = 'a9c5b28b233c43f8bd91a9030e67498d'

geocoder = OpenCageGeoCode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometrylat']['lat']
lat = results[0]['geometrylat']['lng']
print(lat,ing)

myMap = folium.Map(location[lat, ing],zoom_start -9)
folium.Marker([lat, ing], popup=location).add_to(myMap)
myMap.save('Mylocation.html')