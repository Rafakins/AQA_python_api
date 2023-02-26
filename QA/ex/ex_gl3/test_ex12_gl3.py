import requests

class TestEx12Gl3:
    def test_api_header_print(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        assert response.status_code == 200, f"Not 200 status code, status code = {response.status_code}"
        assert "x-secret-homework-header" in response.headers, "Not 'x-secret-homework-header' in headers"
        x_secret_value = response.headers['x-secret-homework-header']
        assert x_secret_value == "Some secret value", "Secret value does not match 'Some secret value'"