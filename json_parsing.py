import json #импортируем библиотеку json для парсинга

string_as_json_format = '{"answer": 30, "name": "Rafael"}' #создаем список в который ложим псевдо json, обрати внимание как пишутся несколько ключей ОДИНАРНЫЕ КАВЫЧКИ ТОЛЬКО ТУТ
object = json.loads(string_as_json_format) #парсим наш список

key = "name" #присваиваем значение ключу

if key in object: #если ключ есть в списке - печатаем его значение
    print(object[key])
else:
    print(f"Ошибка, ключа {key} в JSON нет") #если ключа нет - с помощью f("{}") вставляем переменную key в текст и печатаем аларм


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}' #грузим json
json_text_load = json.loads(json_text) #делаем из json - понятный список для питона
print(json_text_load["messages"][1]["message"]) #отображаем по ключу нужное сообщение, логика такая в "messages" вытащи 1(начинаем с 0) "message", важно помнить, что цифра будет перед сообщением