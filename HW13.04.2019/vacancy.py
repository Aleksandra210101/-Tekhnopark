"""
Creator: Aleksandra Krylova
"""
import requests
import bs4

class Vacancy:
    def __init__(self, speciality, company, skills, location, compensation, publication):
        self.__company = company
        self.__speciality = speciality
        self.__skills = skills
        self.__location = location
        self.__compensation = self.__salary_parser(compensation)
        self.__publication = publication

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def get_company(self):
        return self.__company

    def set_company(self, new_company):
        self.__company = new_company

    def get_skills(self):
        return self.__skills

    def set_skills(self, new_skills):
        self.__skills = new_skills

    def get_location(self):
        return self.__location

    def set_location(self, new_location):
        self.__skills = new_location

    def get_compensation(self):
        return self.__compensation

    def __salary_parser(self, salary):
        temp = salary.split()
        t = (int(temp[0]) + int(temp[1].split('-')[1])) / 2
        t = self.course(temp[-1], t)
        return t

    def course(self, currency, sum):
        """The function that transfers sum from currency to ruble"""
        if currency == "USD":
            url = "https://finance.rambler.ru/currencies/USD/"
        elif currency == "EUR":
            url = "https://finance.rambler.ru/currencies/EUR/"
        else:
            return sum * 1000
        site = requests.get(url)
        soup = bs4.BeautifulSoup(site.text, 'html.parser')
        com = float(soup.find("div", attrs={"class": "finance-currency-plate__currency"}).text.split()[0])
        return com * sum * 1000

    def get_salary(self):
        return self.__compensation


    def set_compensation(self, new_compensation):
        self.__compensation = new_compensation

    def get_publication(self):
        return self.__publication

    def set_publication(self, new_publication):
        self.__publication = new_publication


