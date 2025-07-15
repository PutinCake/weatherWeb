import requests
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()


def get_current_weather(city="Hayward"):
    # print('\n*** Get Current Weather Conditions ***\n')

    # city = input('\nPlease enter the city name: \n')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    print("API_KEY:", os.getenv("API_KEY"))
    weather_data = requests.get(request_url).json()
    # pprint(weather_data)
    return weather_data
    # print(
    #     f'Current weather for {weather_data["name"]}, {weather_data["sys"]["country"]}:')
    # print(f'Temperature: {weather_data["main"]["temp"]}°F')
    # print(
    #     f'Feels like: {weather_data["main"]["feels_like"]}°F, and {weather_data["weather"][0]["description"]}.)')


if __name__ == '__main__':
    print('\n*** Get Current Weather Conditions ***\n')
    city = input('\nPlease enter the city name: \n')

    if not bool(city.strip()):
        city = "Hayward"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
