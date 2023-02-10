import requests

#ГЕТ ЗАПРОС
payload = {"name": "Rafael", "age": 21, "brain": True}
response = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)

try: #пока нет ошибок, выполняем блок ниже
    response_json = response.json()
    print(response_json["name"])
except requests.exceptions.JSONDecodeError: #если наша ошибка - requests.exceptions.JSONDecodeError - печатаем принт ниже.
    print("Response is not a JSON format")
    print(response.text)



#ПОСТ ЗАПРОС - разница в requests.post и data=payload
payload = {"name": "Rafael", "age": 21, "brain": True}
response = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)

try: #пока нет ошибок, выполняем блок ниже
    response_json = response.json()
    print(response_json["name"])
except requests.exceptions.JSONDecodeError: #если наша ошибка - requests.exceptions.JSONDecodeError - печатаем принт ниже.
    print("Response is not a JSON format")
    print (response.text)