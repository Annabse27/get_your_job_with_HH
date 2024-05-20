import pytest


def test_init_vacancy(vacancy_instance_1):
    assert vacancy_instance_1.vacancy_title == "Python Developer"
    assert vacancy_instance_1.town == "Moscow"
    assert vacancy_instance_1.salary_from == 50000
    assert vacancy_instance_1.salary_to == 100000
    assert vacancy_instance_1.currency == "RUB"
    assert vacancy_instance_1.employment == "Full-time"
    assert vacancy_instance_1.url == "https://example.com/vacancy"


def test_vacancy_to_dict(vacancy_instance_1):
    """тестирование метода to_dict"""
    expected_dict = {
        'vacancy_title': "Python Developer",
        'town': "Moscow",
        'salary_from': 50000,
        'salary_to': 100000,
        'currency': "RUB",
        'employment': "Full-time",
        'url': "https://example.com/vacancy"
    }
    assert vacancy_instance_1.to_dict() == expected_dict



def test_vacancy_comparison(vacancy_instance_1, vacancy_instance_2):
    assert vacancy_instance_1 < vacancy_instance_2
    assert vacancy_instance_1 <= vacancy_instance_2
    assert vacancy_instance_1 != vacancy_instance_2
    assert not vacancy_instance_1 == vacancy_instance_2


def test_vacancy_comparison_with_non_vacancy_type(vacancy_instance_1):
    with pytest.raises(TypeError):
        assert vacancy_instance_1 == "not a vacancy"
