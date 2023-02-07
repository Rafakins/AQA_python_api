import requests

response_text = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_json = response_text.json()
    print(parsed_response_json)
except requests.exceptions.JSONDecodeError:
    print("failed")