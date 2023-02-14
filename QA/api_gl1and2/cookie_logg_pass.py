import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
cookie_value = response.cookies.get('auth_cookie') #Метод get()API cookies извлекает информацию об одном файле cookie по его имени и URL-адресу.
print(response.cookies) #ответ - <RequestsCookieJar[<Cookie auth_cookie=245268 for .playground.learnqa.ru/>]>

cookies = {} #создаем пустой словарь, делаем это для того, чтобы можно было безболезнено использовать в cookies = cookies
if cookie_value is not None: #если значение переменной куки_значение не содержит None:
    cookies.update({"auth_cookie": cookie_value}) #апдейтим (добавляем или изменяем) заначения по уже существующим или новым ключам


response_cookie = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)
print(response_cookie.text)




print(response.text)
print(response.status_code)
print(dict(response.cookies))

print(response.headers)

