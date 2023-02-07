import json

string_as_json_format = '{"answer": 30, "name": "Rafael"}'
object = json.loads(string_as_json_format)

key = "name"

if key in object:
    print(object[key])
else:
    print(f"Ошибка, ключа {key} в JSON нет")
