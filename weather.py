import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather2(address):
	api_key=os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
    # get location from address
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude

    #call the forecast.
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° at {}".format(summary, temperature, address)


def get_weather(latitude, longitude, api_key):
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	return "{} and {}".format(forecast.summary, forecast.temperature)


def get_location(address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	return (location.latitude, location.longitude)


#address = input("Please enter an address: ")



#latitude, longitude = get_location(address)
#print (get_weather(latitude, longitude, api_key))
