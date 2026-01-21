# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


def sum_numbers(a: int, b: int) -> int:
    result = a + b
    return result


def mul_numbers(a: int, b: int) -> int:
    result = a * b
    return result


@pytest.mark.usefixtures("show_start_end_datetime")
class TestTask4:
    @pytest.mark.parametrize(
        "a,b,result",
        [
            (8, 2, 10),
            (9, 0, 9),
            (25, -5, 20)
        ]
    )
    def test_1(self, a, b, result, timer):
        assert sum_numbers(a, b) == result

    def test_2(self, timer):
        time.sleep(2)
        assert mul_numbers(5, 5) == 25
