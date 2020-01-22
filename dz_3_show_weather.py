import argparse
import datetime

import requests


api_key='5c92d33463bdb47bd239ae728748d9d7'
parser = argparse.ArgumentParser(description='Shows the weather in the specified city for three days')
parser.add_argument('--city', help='city for which you need to show the weather')
city = parser.parse_args().city

def print_weather_for_day(index_of_day):
	responce = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}')
	responce=responce.json()
	if responce['cod'] == '200':
		day = responce['list'][index_of_day]['dt_txt']
		day = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
		day = day.strftime('%d.%m.%Y')
		temp = responce['list'][index_of_day]['main']['temp']
		temp = ('+' if round(temp) > 0 else '') + str(round(temp))
		weather = responce['list'][index_of_day]['weather'][0]['description']
		text_to_return = f'{day}  {temp}  {weather}'
	else:
		text_to_return = 'Wrong parameter. Try again.'
	return text_to_return

print(print_weather_for_day(0))
print(print_weather_for_day(8))
print(print_weather_for_day(16))