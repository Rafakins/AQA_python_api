import requests #любимый реквест

response_text = requests.get("https://playground.learnqa.ru/api/get_text") #гет запрос, получаем не JSON, а обычный текст
try: #пока нет ошибок, выполняем блок ниже
    parsed_response_json = response_text.json()  #парсим json (эндпоинт отдает текст), так что, получаем ошибку
    print(parsed_response_json)
except requests.exceptions.JSONDecodeError: #если наша ошибка - requests.exceptions.JSONDecodeError - печатаем принт ниже.
    print("Response is not a JSON format")
