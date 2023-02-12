import requests
class PositiveUser: #если назвать класс или функцию с "Test.." или "test_", автоматически запускается пайтест вместо обычного запуска программы

    def logs_user(self):
        name = "Rafael"
        email = "vinkotov@example.com"
        password = "1234"

        url = "https://playground.learnqa.ru/api/user/login"
        data = {
            "email": f"{email}",
            "password": f"{password}"
        }
        response = requests.post(url, data=data)
        print(response.text)
        print(name)

classi = PositiveUser()
classi.logs_user()