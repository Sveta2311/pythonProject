import pytest


from Seminar14.Semin13_Task5 import UserWorkshop
from Seminar14.Exceptions import AccesErorr, LevelError


@pytest.fixture()
def set_up():
    return UserWorkshop()   # данные для теста


def test_access_fail_1(set_up):                               # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr прописан в Exceptions.py

    with pytest.raises(AccesErorr, match='Access denied'):
        set_up.login('Ishkinina', '1')                      # передаются невалидные данные


def test_access(set_up):                                    # тест на проверку валидных данных, что должнo вернуться
    assert set_up.login('Ishkinina', '1') == '5'             # вводятся валидные данные, проверяем на совпадение с результатом


def test_access_fail_2(set_up):                                    # тест на проверку того, что будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr прописан в Exceptions.py
    with pytest.raises(LevelError):
        set_up.login('Ishkinina', '1')
        set_up.create_user('New_user', '1', '3')



if __name__ == '__main__':
    pytest.main(['-v'])