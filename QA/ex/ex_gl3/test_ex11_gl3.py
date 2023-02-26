# Ex11: Тест запроса на метод cookie
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
# Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
# Результатом должна быть ссылка на коммит с тестом.



import requests

class TestEx11Gl3:
    def test_api_cookie_print(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie = response.cookies
        print(cookie)
        assert response.status_code == 200, "Not 200 status code"
        print(response.status_code) # не забывай - что assert, это не if - не нужно табуляция
        assert len(cookie) > 0, "Not cookie a responce"
        assert "Cookie HomeWork=hw_value for .playground.learnqa.ru" in str(cookie) , "Bad Сookie in responce"
