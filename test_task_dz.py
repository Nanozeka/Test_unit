import pytest
from task_dz import AverageCalculator


@pytest.fixture
def calculator():
    return AverageCalculator()


def test_calculate_average_empty(calculator):
    assert calculator.calculate_average([]) == 0


def test_calculate_average_single_element(calculator):
    assert calculator.calculate_average([5]) == 5


def test_calculate_average_average_valid(calculator):
    assert calculator.calculate_average([1, 2, 3]) == 2


def test_compare_averages_first_list_greater(calculator):
    result = calculator.compare_averages([1, 2, 3], [1, 2])
    assert result == "Первый список имеет большее среднее значение"


def test_compare_averages_second_list_greater(calculator):
    result = calculator.compare_averages([1, 2], [1, 2, 3])
    assert result == "Второй список имеет большее среднее значение"


def test_compare_averages_lists_equal(calculator):
    result = calculator.compare_averages([1, 2, 3], [3, 2, 1])
    assert result == "Средние значения равны"

