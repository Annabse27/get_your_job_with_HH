from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """Абстрактный класс для метода получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


