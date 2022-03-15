from urllib import request
import requests
from pprint import pprint

API_KEY = '910350de96ccf2b812a86c40f771f3fa'
city = input('Input your desired city : ')
base_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+API_KEY
weather_map = requests.get(base_url).json()
pprint(weather_map)

'''
read1 = weather_map['weather'][0]['description']
read2 = weather_map['main']['temp']

print("Weather: ",read1)
print("Temperature: ",read2)
'''


