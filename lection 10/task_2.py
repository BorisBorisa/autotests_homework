# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestTask2:
    @pytest.mark.smoke
    def test_1(self):
        assert all_division(8, 2) == 4

    @pytest.mark.smoke
    def test_2(self):
        assert all_division(8, 2, 2) == 2

    @pytest.mark.smoke
    def test_3(self):
        assert all_division(-16, 4, 2) == -2

    def test_4(self):
        assert all_division(100, 50, 2, 1) == 1

    def test_5(self):
        assert all_division(100, 0) == 0

# python -m pytest task_2.py
# python -m pytest task_2.py -m smoke
# python -m pytest task_2.py -k "not 5 and not 1"
