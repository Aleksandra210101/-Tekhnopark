"""
Creator: Aleksandra Krylova
"""

import backend
import parse_hh


if __name__ == "__main__":
    while True:
        VACANCY = input("Я ищу вакансию... ")
        AREA = input("Я ищу в регионе... ")
        backend.names_table(VACANCY, AREA)
        try:
            backend.selector(VACANCY, AREA)
        except:
            parse_hh.hh_parse(VACANCY, AREA)
            backend.selector(VACANCY, AREA)
