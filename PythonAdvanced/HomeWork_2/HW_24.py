from urllib import request
import requests

# получаем содержимое страницы по domain- в качестве порта будет использован 80
# Для указания другого порта используем запись вида: http://example:81.com
response = request.urlopen('https://www.infocar.ua/')

# печатаем информацию об http-ответе
print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# получаем заголовки в виде внутреннего объекта
print(response.headers)
# получаем словарь всех заголовков
print(response.getheaders())
# получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))

response1 = requests.get('https://www.infocar.ua/')
response2 = requests.put('https://www.infocar.ua/')
response3 = requests.post('https://www.infocar.ua/')
response4 = requests.delete('https://www.infocar.ua/')
