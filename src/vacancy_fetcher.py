import logging

import requests

from src import link_api
from src.abstracted_classes import GetVacancies
from src.vacancy import Vacancy

logging.basicConfig(level=logging.INFO)


class VacancyFetcher(GetVacancies):
    """Класс для подключения к сайту HeadHunter"""

    def get_vacancies(self, name_job, pages, per_page=5, start_page=0):
        """
        Получает список вакансий по заданным параметрам.

        Args:
            name_job (str): Название вакансии.
            pages (int): Количество страниц для загрузки.
            per_page (int, optional): Количество вакансий на одной странице. По умолчанию 5.
            start_page (int, optional): Начальная страница для загрузки. По умолчанию 0.

        Returns:
            list: Список объектов Vacancy.
        """
        hh_list = []
        base_params = {
            'text': name_job,
            'per_page': per_page
        }

        for page in range(start_page, start_page + pages):
            params = dict(base_params, page=page)
            try:
                response = requests.get(link_api, params=params)
                response.raise_for_status()
                response_data = response.json()
                logging.info(f"Получен ответ на страницу {page + 1}")
            except requests.RequestException as e:
                logging.error(f"Произошла ошибка при получении данных API: {e}")
                continue

            for item in response_data.get('items', []):
                hh_vacancy = self._parse_vacancy(item)
                if hh_vacancy:
                    hh_list.append(hh_vacancy)

        return hh_list

    def _parse_vacancy(self, item):
        """Парсит отдельную вакансию из данных"""
        try:
            title = item.get('name', 'Noname Title')
            town = item.get('area', {}).get('name', 'Noname Town')
            salary = item.get('salary', {})
            salary_from = salary.get('from', 0) if salary else 0
            salary_to = salary.get('to', 0) if salary else 0
            currency = salary.get('currency', 'Noname Currency') if salary else 'Noname Currency'
            employment = item.get('employment', {}).get('name', 'Noname Employment Type')
            url = item.get('alternate_url', '#')

            return Vacancy(title, town, salary_from, salary_to, currency, employment, url)
        except KeyError as err:
            logging.error(f"Ошибка ожидаемых данных: {err}")
            return None
