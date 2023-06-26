'''
This class will serve as the foundation for our weather app. We will use the website 'OpenWeatherMap' API in order to grab our weather forecast data.

API KEY: 3d457d463e8f2a568c8717d8e9947002
'''

import requests

class getWeather:
    
    location = ''
    temp_high = 0
    temp_low = 0
    wind_speed = 0
    humidity = 0
    description = ''
    sunrise = ''
    sunset = ''
 
    
    def __init__(self,api_key,city,zip_code):
        super().__init__()
        
        self.city = city
        self.zip_code = zip_code
        self.api_key = api_key
        self.getForecast(self.api_key,self.city,self.zip_code)
        
    def getForecast(self,api_key,city,zip_code):
        weather_url = "https://api.openweathermap.org/data/2.5/weather"
        
        parameters = {
            'APPID':api_key,
            'units':'imperial',
            'zip':zip_code,
            'q':city
        }
        
        api_response = requests.get(weather_url,params=parameters)
        weather_data = api_response.json()
        
        '''
        {'coord': {'lon': -78.9591, 'lat': 43.0183}, 
        'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
        'base': 'stations', 
        'main': {'temp': 79.86, 'feels_like': 79.86, 'temp_min': 75.13, 'temp_max': 82.36, 'pressure': 1019, 'humidity': 52},
        'visibility': 10000, 
        'wind': {'speed': 13.8, 'deg': 60}, 
        'clouds': {'all': 0}, 
        'dt': 1687300046, 
        'sys': {'type': 2, 'id': 2007677, 'country': 'US', 'sunrise': 1687253788, 'sunset': 1687309093},
        'timezone': -14400, 
        'id': 0, 
        'name': 'Grand Island', 
        'cod': 200}
        '''
                
        if api_response.status_code == 200:
            self.location = weather_data['name']
            self.temp_high = weather_data['main']['temp_max']
            self.temp_low = weather_data['main']['temp_min']
            self.wind_speed = weather_data['wind']['speed']
            self.humidity = weather_data['main']['humidity']
            self.description = weather_data['weather']['description']
            self.sunrise = weather_data['sys']['sunrise']
            self.sunset = weather_data['sys']['sunset']
        else:
            print('An error occured while fetching the weather data.')
            
#--------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    #x = getWeather('d4b7ac38f8d6e6555ad50e43cb755352','','14072')
        