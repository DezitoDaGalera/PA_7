from bs4 import BeautifulSoup
import requests
import string
import urllib
from .json_parser import parser

class scraper:
    def __init__(self):
        super().__init__()

    def text_scraper(self):
        
        final_text=""
        search = requests.get(r'https://www.cgesp.org/v3/alagamentos.jsp?dataBusca=10%2F02%2F2020&enviaBusca=Buscar')
        #search = requests.get(r"https://www.cgesp.org/v3/alagamentos.jsp")

        soup = BeautifulSoup(search.text, 'lxml')

        final_text=final_text + soup.body.text.upper()

        return final_text

class matcher:
    def __init__(self):
        super().__init__()

    def retrieve(self):
        data_parser = parser()
        data = data_parser.parse()
        text_scraper = scraper()
        final_text = text_scraper.text_scraper()
        locations = []
        if "Não há registros de alagamentos para essa data.".upper() in final_text:
            locations.append({"Name":"","Value":"Não há registros de alagamentos hoje"})
        else:
            for info in data:
                if info["Value"].upper() in final_text:
                    if info["Value"].upper not in locations:
                        locations.append(info)

        return locations
