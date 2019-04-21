"""
Creator: Aleksandra Krylova
"""
import time
import requests as r
from bs4 import BeautifulSoup as bs
import backend



def create_session(url):
    """The function that create session and return html"""
    headers = {"accept": "*/*",
               "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36"
                             " (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    session = r.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.text, 'html.parser')
        return soup


def area_num(text, uarea):
    """The function returns the link with the correct number of area(uarea)"""
    url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&search_period=30&text=' + text
    soup = create_session(url)
    area = soup.find_all('span', attrs={'class': 'clusters-value__name'})
    for i in area:
        if i.text == uarea:
            return i.parent['href']       #?clusters=true&enable_snippets=true&text=Python&area=4&from=cluster_area


def url_page(text, area):
    """The function that return list of urls with correct page"""
    urls = []
    url_end = area_num(text, area)
    base_url = 'https://hh.ru/search/vacancy' + url_end
    soup = create_session(base_url)
    try:
        page = soup.find_all('a', attrs={'data-qa':'pager-page'})
        end = int(page[-1].text)
        for i in range(0, end + 1):
            urls.append(f'https://hh.ru/search/vacancy' + url_end + '&page=' + str(i))
    except:
        urls = ['https://hh.ru/search/vacancy' + url_end]
    return urls


def hh_parse(text, area):
    """The function that  create table "text",  parse data and add all correct data in table"""
    jobs = []
    num = 0
    backend.create_table(text, area)
    for url in url_page(text, area):
        soup = create_session(url)
        divs = soup.find_all("div", attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"}).text
            href = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"})['href']
            requirement = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"}).text
            date = div.find("span", attrs={"class": "vacancy-serp-item__publication-date"}).text
            empolyer = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-employer"}).text
            try:
                compensation = div.find("div", attrs={"class": "vacancy-serp-item__compensation"}).text
            except:
                compensation = '-'
            jobs.append({'title: ': title,
                         'href: ': href,
                         'empolyer: ': empolyer,
                         'requirement: ': requirement,
                         'compensation: ': compensation,
                         'date': date})
            backend.add_line(text, title, empolyer, requirement, compensation, date, href, area)
            num = num + 1
        backend.num(text, area, num)


def autoupdate():
    """The function that updates data in tables in data base"""
    while True:
        try:
            for i in backend.selector_nt():                                           #перебираем имя таблиц
                hrefend = backend.selector_href(i[0], i[1])
                jobs = []
                num = 0
                backend.create_table(i[0], i[1])
                for url in url_page(i[0], i[1]):
                    soup = create_session(url)
                    divs = soup.find_all("div", attrs={'data-qa': 'vacancy-serp__vacancy'})
                    for div in divs:
                        href = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"})['href']
                        if href != hrefend:
                            title = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"}).text
                            requirement = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"}).text
                            date = div.find("span", attrs={"class": "vacancy-serp-item__publication-date"}).text
                            empolyer = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-employer"}).text
                            try:
                                compensation = div.find("div", attrs={"class": "vacancy-serp-item__compensation"}).text
                            except:
                                compensation = '-'
                            jobs.append({'title: ': title,
                                         'href: ': href,
                                         'empolyer: ': empolyer,
                                         'requirement: ': requirement,
                                         'compensation: ': compensation,
                                         'date': date})
                            num = num + 1
                            backend.add_line(i[0], title, empolyer, requirement, compensation, date, href, i[1])
                    backend.num(i[0], i[1], num)
        except:
            pass
        time.sleep(86400)
