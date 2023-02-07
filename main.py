from json.decoder import JSONDecodeError
import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response_json = response.json()

key = "answer"

if key in parsed_response_json:
    print(parsed_response_json[key])
else:
    print(f"Ошибка,  ключа {key} в JSON нет")



response_text = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_json = response_text.json()
    print(parsed_response_json)
except JSONDecodeError:
    print("Response is not a JSON format")