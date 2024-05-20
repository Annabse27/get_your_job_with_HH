from functools import total_ordering


@total_ordering
class Vacancy():
    """
    Информация о вакансии
    """

    def __init__(self, vacancy_title, town, salary_from, salary_to, currency, employment, url):
        self.vacancy_title: str = vacancy_title
        self.town: str = town
        self.salary_from: int = self.validate_salary(salary_from)
        self.salary_to: int = self.validate_salary(salary_to)
        self.currency: str = currency
        self.employment: str = employment
        self.url: str = url

    @staticmethod
    def validate_salary(salary):
        if not isinstance(salary, int) or salary is None:
            return 0
        return salary

    def __str__(self):
        if self.salary_from == 0 and self.salary_to == 0:
            salary_info = "зарплата не указана"
        elif self.salary_from == 0:
            salary_info = f'Зарплата до: {self.salary_to} {self.currency}'
        elif self.salary_to == 0:
            salary_info = f'Зарплата от: {self.salary_from} {self.currency}'
        else:
            salary_info = f'Зарплата от: {self.salary_from} до: {self.salary_to} {self.currency}'

        return f'Название вакансии: {self.vacancy_title}\n' \
               f'Город: {self.town}\n' \
               f'{salary_info}\n' \
               f'Тип занятости: {self.employment}\n' \
               f'Ссылка на вакансию: {self.url}\n'

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("not a vacancy")
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("not a vacancy")
        return self.salary_from < other.salary_from

    # Добавьте другие методы сравнения при необходимости

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            'vacancy_title': self.vacancy_title,
            'town': self.town,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency,
            'employment': self.employment,
            'url': self.url
        }


if __name__ == "__main__":
    pass
