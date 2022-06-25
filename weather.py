import requests

API_KEY = '6b680195e8a66017f1dc3195395da353'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter your city: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print('Weather', weather)
    print('Temperature', temperature, 'celsius')
else:
    print('An error occurred')

git config --global user.email "ayobamisamuel58@gmail.com"
git config --global user.name "YAyobami"
