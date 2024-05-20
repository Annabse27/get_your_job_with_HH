import logging
import json


from src.vacancy_fetcher import VacancyFetcher

logging.basicConfig(level=logging.INFO)


class VacancySearchApp:
    """
    Основной класс для работы с вакансиями через API HeadHunter.
    """

    def __init__(self):
        """
        Инициализирует объект VacancySearchApp.

        Переменные экземпляра:
        - hh_api: экземпляр класса VacancyFetcher для работы с API HeadHunter.
        - current_page: текущая страница вакансий для пагинации.
        - vacancies: список всех найденных вакансий.
        """
        self.hh_api = VacancyFetcher()
        self.current_page = 0
        self.vacancies = []

    def active_fetch_vacancies(self):
        """
        Запускает режим выбора пользователем вакансий.

        Пользователь вводит название профессии и количество страниц для вывода вакансий.
        Выводит вакансии на экран и предлагает продолжить поиск или завершить программу.
        Если введено значение 0, выводит 30 топ вакансий и завершается.
        """
        while True:
            keyword = input('Напишите название профессии: \n')
            pages_input = input('Сколько вывести страниц? (Введите 0 или оставьте пустым для вывода 30 топ вакансий)\n')

            try:
                pages = int(pages_input) if pages_input else 0
            except ValueError:
                pages = 0

            if pages == 0:
                self.current_page = 0
                self.get_and_print_vacancies(keyword, pages)
                print('Спасибо за использование программы! Ваш поиск сохранен в файле vacancies.json')
                self.save_to_json()
                break
            else:
                self.get_and_print_vacancies(keyword, pages)

            user_answer = input('Хотите продолжить поиск вакансий? Да/Нет \n').lower()
            if user_answer != 'да':
                print('Спасибо за использование программы! Ваш поиск сохранен в файле vacancies.json')
                self.save_to_json()
                break
            else:
                self.current_page += pages

    def get_and_print_vacancies(self, keyword, pages):
        """
        Получает и выводит вакансии в соответствии с запросом пользователя.

        Аргументы:
        - keyword: строка, ключевое слово для поиска вакансий.
        - pages: целое число, количество страниц для вывода вакансий.

        Выводит информацию о вакансиях на экран.

        """
        if pages == 0:
            print('Выведено 30 топ вакансий:')
            self.vacancies = self.hh_api.get_vacancies(keyword, 6, per_page=5)
        else:
            self.vacancies.extend(self.hh_api.get_vacancies(keyword, pages, start_page=self.current_page))

        self.vacancies.sort(key=lambda x: (x.salary_to if x.salary_to else 0, x.salary_from if x.salary_from else 0),
                            reverse=True)

        print('Список вакансий с сайта "HeadHunter": \n')
        for idx, vacancy in enumerate(self.vacancies, start=1):
            print(f"{idx}. {vacancy}")

    def save_to_json(self):
        """
        Сохраняет все найденные вакансии в файл JSON.

        Создает файл 'vacancies.json' и записывает в него список словарей,
        содержащих информацию о каждой вакансии.
        """
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump([vars(v) for v in self.vacancies], file, ensure_ascii=False, indent=4)


