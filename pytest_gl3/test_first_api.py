import requests
import pytest #используем для перебора кортежа

class TestFirstApi: # создаем класс в которую пихаем функцию (наш тест)

    # массив - это структура данных, в которой хранятся значения данных ОДНОГО типа
    # список - это структура данных, в которой могут хранится значение ПРОИЗВОЛЬНОГО ТИПА
    # кортеж - это НЕИЗМЕНЯЕМЫЙ СПИСОК (защита от дурака)
    # при указании кортежа (между классом и функцией), pytest будет автоматически перебирать каждое значение кортежа, что позволяет параметризировать тесты

    names = [ # это кортеж с данными
        ("Rafael"),
        ("Valeria"),
        ("Fail"),
        ("")
    ]
    @pytest.mark.parametrize('name', names) # указываем сначала имя переменной, в которую будем передавать данные, потом переменную, из которой эти данные будем брать.
    # @pytest.mark.parametrize - функция декоратор из pytest
    def test_hello_call(self, name): # создаем функцию с названием self (такая традиция, но нужно разобраться), указываем переменную которая будет приходить из вне
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong responce code" # сравниваем статус код (первая проверка), у каждой ошибки должно быть свое конкретное описание, чтобы точно определить на провале, где ошибка

        response_dict = response.json() #dict - словарь (прим перевод). Сразу переводим в json. Дополнительно распаршевать не нужно
        assert "answer" in response_dict, "There is no field 'answer' in the response" #ошибка 2лвл - проверяем наличие поле answer(ответ), прежде чем сравнивать само значение этого поля

        if len(name) == 0:
            expected_responce_text = "Hello, someone"
        else:
            expected_responce_text = f"Hello, {name}" #любимый f <З, пишем ожидаемый ответ - текст
        actual_response_text = response_dict["answer"] #вытаскиваем из уже распаршенного json - значение по ключу "answer"
        assert actual_response_text == expected_responce_text, "Actual  text in the responce is not correct" #ошибка 3 уровня - проверяем соответствие значения поля answer - с ожидаемым значением из переменной (его мы должны знать заранее)

#python -m pytest test_first_api.py -k test_hello_call                   - START
# Опцию -k командной строки можно использовать, чтобы указать подстроку, которая должна присутствовать в именах тестов (при использовании опции -m проверяется точное совпадение). Это облегчает отбор тестов по именам.