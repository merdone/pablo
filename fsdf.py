from pyowm import OWM
import math

API_KEY = '8f213837566bfaa18be4e2640ab33762'
owm = OWM(API_KEY)
PLACE_CITY = input('Яке місто шукаєте?')

manage = owm.weather_manager()
data = manage.weather_at_place(PLACE_CITY)
weather = data.weather
temperature = weather.temperature('celsius')
temp = math.floor(temperature['temp'])
print(temp)