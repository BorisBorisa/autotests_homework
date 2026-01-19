# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestTask3:
    @pytest.mark.parametrize(
        "a,b,result",
        [
            (8, 2, 4),
            pytest.param(9, 3, 3, marks=pytest.mark.smoke),
            pytest.param(25, 5, 5, marks=pytest.mark.skip('broken'))
        ]
    )
    def test_1(self, a, b, result):
        assert all_division(a, b) == result

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
