import requests

headers = {"some_header": "True"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
print(response.text)
print(response.headers) #показывает хедеры отправленные сервером нам