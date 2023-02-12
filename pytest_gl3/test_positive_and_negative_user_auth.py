import requests
import pytest
class TestPositiveUser:

    #параметры выносим до всех функций (независимо от того, в каком тесте мы вызываем этот параметр
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self): #функция setup  в которую мы закладываем все что у нас дублируется в будущих тестах
        email = "vinkotov@example.com"
        password = "1234"

        data = {
            "email": f"{email}",
            "password": f"{password}"
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert response_login.status_code == 200, "Wrong responce code"
        assert "user_id" in response_login.json(), "There is no 'user_id' in the response"

        self.cookie_value = response_login.cookies.get('auth_sid')
        self.csrf_token_value = response_login.headers.get('x-csrf-token')
        self.user_id_from_auth_method = response_login.json()["user_id"]

    #self. - это указатель, позволяющий делать переменную полем класса - в следствии, передавать значени из одной функции в другие, ставится перед переменной при ее присвоении и в дальнейшем во время ее инициализации

    def test_auth_user(self):

        cookie = {
            "auth_sid": f"{self.cookie_value}"
        }
        headers = {
            "x-csrf-token": f"{self.csrf_token_value}"
        }

        response_auth = requests.get("https://playground.learnqa.ru/api/user/auth", cookies=cookie, headers=headers)

        assert response_auth.status_code == 200, "Wrong responce code"
        assert "user_id" in response_auth.json(), "There is no 'user_id' in the response"
        assert self.user_id_from_auth_method == response_auth.json()["user_id"], "Unique user identifiers do not match"
        # если мы указываем респонс.куки можем сразу парсить ('нужный заголовок') - куки, также и с хедерами и с .json()["хуадер"]



    @pytest.mark.parametrize('condition', exclude_params) # внутри теста будет переменная, которая будет равна либо no_cookie, либо no_token - прогоняем каждое значение кортежа в тесте

    #!!!!
    # @ - декоратор
    # @pytest.mark.parametrize - фикстура, это некое предусловие, которое подготавливает окружение (стенд), переменные и все такое, перед запуском тестов
    #!!!

    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            cookie = {
                "auth_sid": ""
            }

            headers = {
                "x-csrf-token": f"{self.csrf_token_value}"
            }

            response_auth = requests.get("https://playground.learnqa.ru/api/user/auth", cookies=cookie, headers=headers)
            assert response_auth.status_code == 200, "Wrong responce code"
            assert "user_id" in response_auth.json(), "There is no user id in the second responce"


        elif condition == "no_token":
            cookie = {
                "auth_sid": f"{self.cookie_value}"
            }

            headers = {
                "x-csrf-token": ""
            }

            response_auth = requests.get("https://playground.learnqa.ru/api/user/auth", cookies=cookie, headers=headers)
            assert response_auth.status_code == 200, "Wrong responce code"
            assert "user_id" in response_auth.json(), "There is no user id in the second responce"

            user_id_from_check_method = response_auth.json()["user_id"]

            assert user_id_from_check_method == 0, f"User is authorized  with condition {condition}"