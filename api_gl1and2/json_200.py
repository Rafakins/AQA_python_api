import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True) #allow_redirects - указывает разрешен ли нам редирект (по-умолчанию всегда ДА)
first_response = response.history[0] #показывает историю редиректов, указываем, что нам интересен первый редирект
print(first_response.url) #выводим именно url первого редиректа
print(response.url )#выводим конечный url

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
print(first_response.url)
first_response = response.history[1]
print(first_response.url)
print(response.url)