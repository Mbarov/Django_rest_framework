import requests
from django.core.exceptions import ObjectDoesNotExist
from .models import Street, City


#получение id города (по базе kladr)
def get_city_id(city_name):
    url = 'https://kladr-api.ru/api.php?query={}&contentType=city&typeCode=1'
    result = requests.get(url.format(city_name)).json()
    city_id = result['result'][1]['id'] #индекс 1 т.к. под 0 индексом выводится 'Бесплатная версия kladr-api.ru'
    return city_id

#создание обьекта города или нахождение существующего
def get_city_object(city_name):
    try:
        city = City.objects.get(name=city_name)
    except ObjectDoesNotExist:
        city = City.objects.create(name=city_name)
        city.save()
    return city

#нахождение всех улиц города
def get_streets(city_id):
    url = 'https://kladr-api.ru/api.php?cityId={}&contentType=street'
    result = requests.get(url.format(city_id)).json()
    return result

#Импорт улиц города 
def get_all_streets(requests, city_name):
    city_id = get_city_id(city_name)
    city_obj = get_city_object(city_name)
    result = get_streets(city_id)
    for x in result['result']:
        street = Street.objects.create(name=x['name'], city=city_obj)
        street.save()
    return street

