# Написать функцию, которая производит поиск и выводит на экран вакансии
# с заработной платой больше введённой суммы 
# (необходимо анализировать оба поля зарплаты). 

from task_1 import ScrapingJob
from pprint import pprint

vacancy_db = ScrapingJob('mongodb://172.17.0.2:27017/', 'vacancy', 'vacancy_db')

vacancy_db.print_salary(300_000)
