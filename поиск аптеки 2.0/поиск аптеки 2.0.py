import sys
from io import BytesIO
import requests
from PIL import Image
from map import get_coordinates, get_length

toponym_to_find = "Стерлитамак, проспект Октября 1"

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
if not response:
    print('error')
    exit()

min_length = 50000000
obj = None
for item in response.json()["features"]:
    length = get_length(*ll, *item["geometry"]["coordinates"])
    if length < min_length:
        min_length = length
        obj = item

point = ",".join([str(v) for v in obj["geometry"]["coordinates"]])
map_params = {
    "ll": f"{ll[0]},{ll[1]}",
    "spn": f"{4*spn[0]},{4*spn[1]}",
    "l": "map",
    "pt": point + ",pm2dgl~" + f"{ll[0]},{ll[1]},pm2dgl"
}

print(obj["properties"]["name"])
print(obj["properties"]["CompanyMetaData"]["Hours"]["text"])
print(min_length, "м.")

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
