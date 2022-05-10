from io import BytesIO
import requests
from PIL import Image
from map import get_coordinates, get_length

toponym_to_find = input()
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    print('error')
    exit()

json_response = response.json()
ll, spn = get_coordinates(json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"])

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": f"{ll[0]},{ll[1]}",
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()

pharmacy_dict = {'no_data': [],
                 'twenty_four_hours': [],
                 'not_twenty_four_hours': []}

points = ''

for i in json_response['features']:
    point = ",".join([str(v) for v in i["geometry"]["coordinates"]])
    try:
        time = i['properties']['CompanyMetaData']['Hours']['Availabilities'][0]
        try:
            if bool(i['properties']['CompanyMetaData']['Hours']['Availabilities'][0]['TwentyFourHours']):
                points += point + ",pm2gnl~"
        except KeyError:
            points += point + ",pm2bll~"
    except KeyError:
        points += point + ",pm2grl~"

print(points)
map_params = {
    "ll": f"{ll[0]},{ll[1]}",
    "spn": f"{4*spn[0]},{4*spn[1]}",
    "l": "map",
    "pt": points[:-1]
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()

