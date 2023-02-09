import requests

params = {"method": "DELETE"}

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = params)
print(response.text)

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = params)
print(response.text)

response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = params)
print(response.text)

response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = params)
print(response.text)