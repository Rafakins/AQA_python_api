import json.decoder

from requests import Response #ИЗ библиотеки реквест - импортируем ОДНО поле класса, вместо набора всх функций, это позволяет при обращении к созданному классу не перебирать все что есть
#создали директорию либ, в нее будем создавать файлы, к которым в последствии будем обращаться, начало создания своего фраемворка
#обращаю внимание, что теперь названия классов и методов начинаются не с Test или test_
class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookie, f"Cannon find cookie with name {cookie_name} in the last responce"
        return response.cookie[cookie_name]
    def get_header(self, response: Response,headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last responce"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = Response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Responce is not JON Format. Responce text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]


print(__name__)
#переменная показывает нам, запускается ли файл как основной (при нахождении в нем) или вызывавается через импорт
if __name__ == "__main__":
    print("условие выполняется только когда файл запускается как основной (main)")
elif __name__ != "__main__":
    print("условие выполняется только когда файл запускается через import!")