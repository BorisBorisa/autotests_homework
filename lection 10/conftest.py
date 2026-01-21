import pytest

from datetime import datetime
from time import perf_counter


@pytest.fixture(scope="class")
def show_start_end_datetime():
    print(f"Время начала тестов {datetime.now()}")
    yield
    print(f"Время окончания тестов{datetime.now()}")


@pytest.fixture
def timer():
    start_time = perf_counter()
    yield
    end_time = perf_counter()
    print(f"Время затраченное на тест -> {round(end_time - start_time, 6)} секунд")
