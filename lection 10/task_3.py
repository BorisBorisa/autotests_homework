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
        "args,result",
        [
            ((8, 2), 4),
            ((100, 50, 2), 1),
            ((-16, 4, 2), -2),
            pytest.param((9, 3), 3, marks=pytest.mark.smoke),
            pytest.param((100, 0), 0, marks=pytest.mark.skip('broken'))
        ]
    )
    def test(self, args, result):
        assert all_division(*args) == result
