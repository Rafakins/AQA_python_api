import requests

class TestFirstApi: # создаем класс в которую пихаем функцию (наш тест)
    def test_hello_call(self): # создаем функцию с названием self (такая традиция, но нужно разобраться)
        url = "https://playground.learnqa.ru/api/hello"
        name = "Rafael"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong responce code" # сравниваем статус код (первая проверка), у каждой ошибки должно быть свое конкретное описание, чтобы точно определить на провале, где ошибка

        response_dict = response.json() #dict - словарь (прим перевод). Сразу переводим в json. Дополнительно распаршевать не нужно
        assert "answer" in response_dict, "There is no field 'answer' in the response" #ошибка 2лвл - проверяем наличие поле answer(ответ), прежде чем сравнивать само значение этого поля

        expected_responce_text = f"Hello, {name}" #любимый f <З, пишем ожидаемый ответ - текст
        actual_response_text = response_dict["answer"] #вытаскиваем из уже распаршенного json - значение по ключу "answer"
        assert actual_response_text == expected_responce_text, "Actual  text in the responce is not correct" #ошибка 3 уровня - проверяем соответствие значения поля answer - с ожидаемым значением из переменной (его мы должны знать заранее)

#python -m pytest test_first_api.py -k test_hello_call                   - START