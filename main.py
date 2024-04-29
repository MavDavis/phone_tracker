import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from myphone import number

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")

from phonenumbers import carrier
# service_provider = phonenumbers.parse(number)

from opencage.geocoder import OpenCageGeocode
key = 'c980868b12d2419fb45896f13d3d2fcf'
geocoder = OpenCageGeocode(key)
query  = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat,lng], popup=location).add_to(myMap)
myMap.save("myLocation.html")