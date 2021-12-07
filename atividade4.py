#!/usr/bin/python3
'''
ATIVIDADE: Realizar uma busca de vagas no LINKEDIN passando um determinado tipo.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RoboEmprego():
    def __init__(self):
        self.webdriver = webdriver.Firefox()

    def busca(self, busca, paginas):
        videos = []
        pagina =1
        url ="https:/br.linkedin.com/jobs/search?keywords=%s" % busca
        self.webdriver.get(url)

        while pagina <= paginas:
            titulos = self.webdriver.find_elements_by_xpath("//a[@id='aria-label']")
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Empregos encontrados: %s" % titulo.text) 
                    videos.append(titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print("Mundando para a página %s" % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scroll(0,%s);" % bottom)
        time.sleep(5)

bot = RoboEmprego()
#Passando parametro para buscar o tipo de emprego
bot.busca("financeiro",5)
