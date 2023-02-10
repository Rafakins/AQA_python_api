from json.decoder import JSONDecodeError #импортируем ошибку (?)
import requests

payload = {"name": "User"} #устанавливаем параметры для гет запроса
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload) #отправляем Гет запрос на АПИ с необходимыми параметрами
parsed_response_json = response.json() #парсим json из ответа эндпоинта

key = "answer" #ключ - заголовок (хедер)

if key in parsed_response_json: #если ключ есть в спаршеном json - печатаем его
    print(parsed_response_json[key])
else:
    print(f"Ошибка,  ключа {key} в JSON нет") #если ключа нет - с помощью f("{}") вставляем переменную key в текст и печатаем аларм



response_text = requests.get("https://playground.learnqa.ru/api/get_text") #отправляем гет запрос на другой эндпоинт
try: #пока нет ошибок, выполняем блок ниже
    parsed_response_json = response_text.json()  #парсим json (эндпоинт отдает текст), так что, получаем ошибку
    print(parsed_response_json)
except JSONDecodeError: #если наша ошибка заканчивается на JSONDecodeError - печатаем принт ниже. Такой код возможен при импорте ошибки - from json.decoder import JSONDecodeError, пока не совсем понятно, зачем так делать
    #ошибку выше можно не ипортировать, а записать полностью - requests.exceptions.JSONDecodeError
    print("Response is not a JSON format")