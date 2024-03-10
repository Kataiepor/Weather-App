import requests
from datetime import datetime, timedelta

api_key = '09e8833132ee35d39cd83f816d0514a2'

print("Hello")

city = input("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found, Try Again")
else:
    weather_info = weather_data.json()
    weather = weather_info['weather'][0]['main']
    temp = weather_info['main']['temp']
    feels_like = weather_info['main']['feels_like']

    # Fahrenheit to Celsius Converter
    temp = (temp - 32) / (9/5)
    temp = round(temp)
    feels_like = (feels_like - 32) / (9/5)
    feels_like = round(feels_like)

    # Get the local time for the city using the timezone information provided by OpenWeatherMap API
    timestamp = weather_info['dt']
    city_time = datetime.utcfromtimestamp(timestamp) + timedelta(seconds=weather_info['timezone'])

    print(f"The weather in {city} is: {weather}")
    print(f"The Temperature is {temp} °C")
    print(f"The Feel Like Temperature is {feels_like} °C")
    print(f"Local Time in {city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')}")