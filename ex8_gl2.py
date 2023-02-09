import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json = (response.json())
token = json["token"]
seconds = json["seconds"]
print(json)
time.sleep(0)

params = {"token": token}
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=params)
print(response.text)
if str(response.text) != str('"{"status":"Job is NOT ready"}"'):
    print("Успех")
elif str(response.text) == str('"{"status":"Job is NOT ready"}"'):
    print("Не Успех")
else:
    print("Говно")
#разобраться с сравнением