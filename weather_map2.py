from urllib import request, response
from wsgiref.util import request_uri
import requests 

API_KEY = '910350de96ccf2b812a86c40f771f3fa'

base_url = 'http://api.openweathermap.org/data/2.5/weather/'

city = input("Enter your desired city : ")

request_url = f"{base_url}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print ("Weather: ",weather)
    print ("Temperature: ",temperature, "celcius")
else:
    print ("An Error occured")