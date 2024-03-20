#first install phonenumbers,folium and opencage in your terminal or cmd
import phonenumbers
import folium
from phonenumbers import geocoder

#the key will enable you to use the opencage module requests
#this part of code shows the country of the phone number

key = "paste your key from opencage.com"
number=input("Enter phone number with country code:")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)


#this part of code shows the service provider for the number

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))


#this part of code shows the latitude and longitude coordinates of the number

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat , lng)


#this code save the latitude and longitude coordinates in an html file and shows the position in the map

map_location = folium.Map(location = [lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup = number_location).add_to(map_location)
map_location.save("location.html")
