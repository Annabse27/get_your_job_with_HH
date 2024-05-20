import pytest
from src.vacancy import Vacancy



@pytest.fixture
def vacancy_instance_1():
    return Vacancy(
        vacancy_title="Python Developer",
        town="Moscow",
        salary_from=50000,
        salary_to=100000,
        currency="RUB",
        employment="Full-time",
        url="https://example.com/vacancy"
    )


@pytest.fixture
def vacancy_instance_2():
    return Vacancy(
        vacancy_title="Java Developer",
        town="St. Petersburg",
        salary_from=60000,
        salary_to=120000,
        currency="RUB",
        employment="Remote",
        url="https://example.com/vacancy2"
    )



