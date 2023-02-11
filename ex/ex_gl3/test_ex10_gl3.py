class TestEx10Gl3: # Класс должен начитаться с Test, иначе - не работает
    def test_short_phrase(self): # функция должна начинаться с test_, иначе - не работает
        phrase = input("Set a phrase: ")
        characters = len(phrase)
        assert characters < 15, "Phrase longer than 15 characters"

# cd ../..
# python -m pytest -s test_ex10_gl3.py
# -s перед названием файла теста - используется для того, чтобы не скипать print (тест стопается до введения значения)