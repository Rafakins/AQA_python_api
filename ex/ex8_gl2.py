import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json = (response.json())  #парсим из гет запроса json
token = json["token"] #вытаскиваем по ключу значение json (как-то отдельно преобразовывать json в список не нужно)
seconds = json["seconds"] #вытаскиваем по ключу значение json (как-то отдельно преобразовывать json в список не нужно)
print(json)
time.sleep(seconds) #спим спаршенное из запроса время

params = {"token": token} #формируем параметры для гет запроса
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=params)
json = response.json() #получаем json
status = json["status"] #вытаскиваем по ключу значение json (как-то отдельно преобразовывать json в список не нужно)
if str(status) != "Job is NOT ready": #переводим статус к строке и проверяем наличие слов
    print("Успех")
    print(response.json())
    if str("result") in str(response.json()): #если в строке json есть ключ result - то
        print("Результат есть")


else:
    print("Что-то пошло не так")
    if str("result") in str(response.json()):
        print("Результат есть")
    else:
        print("Результата нет")
