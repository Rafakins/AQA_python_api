import requests

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_505")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_404")
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
print(first_response.url)
print(response.url)