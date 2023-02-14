from requests import Responce #ИЗ библиотеки реквест - импортируем ОДНО поле класса, вместо набора всх функций, это позволяет при обращении к созданному классу не перебирать все что есть
#создали директорию либ, в нее будем создавать файлы, к которым в последствии будем обращаться, начало создания своего фраемворка
#обращаю внимание, что теперь названия классов и методов начинаются не с Test или test_
class BaseCase:
    def get_cookie(self, responce: Responce, cookie_name):
        assert cookie_name in responce.cookie, f"Cannon find cookie with name {cookie_name} in the last responce"
        return responce.cookie[cookie_name]
    def get_header(self, response: Responce,headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last responce"
        return response.headers[headers_name]