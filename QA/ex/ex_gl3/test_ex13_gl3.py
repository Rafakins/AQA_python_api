import requests
import pytest
import json

class TestEx13Gl3:

    #создаем кортеж по формату [(элемент1, элемент2),(элемент1, элемент2),(элемент1, элемент2)]
    headers = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', "'platform': 'Mobile', 'browser': 'No', 'device': 'Android'"),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', "'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', "'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'"),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', "'platform': 'Web', 'browser': 'Chrome', 'device': 'No'"),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', "'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'")
    ]

    #указываем сначала имя переменной, в которую будем передавать данные, потом переменную, из которой эти данные будем брать.
    @pytest.mark.parametrize('header', headers)
    def test_auth_user_agent(self, header):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url,headers={"User-Agent": header[0]}) #обращаемся к первому элементу из переменной с кортежа
        assert response.status_code == 200, "Wrong responce code"
        response_dict = response.json()
        assert "platform" in response_dict, "There is no field 'platform' in the response"
        print(header[1:]) #изи способ вывести все элементы кроме первого (под индексом 0)
        assert response_dict["platform"] in str(header[1:]), f"Title 'platform' does not match" #обращаю внимание, что для проверки используется обращение к json через переменную
        assert response_dict["browser"] in str(header[1:]), f"Title 'browser' does not match"
        assert response_dict["device"] in str(header[1:]), f"Title 'device' does not match"
    # python -m pytest -s test_ex13_gl3.py

