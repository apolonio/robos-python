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
        vagas = []
        pagina =1

        url ="https:/br.linkedin.com/jobs/search?keywords=%s"
        self.webdriver.get(url)

      
        campo = self.webdriver.find_element_by_xpath("//input[@aria-label='Pesquisar cargos ou empresas']")
        campo.send_keys(busca)
        campo.send_keys(Keys.ENTER)
        time.sleep(3)

        lista = self.webdriver.find_elements_by_xpath("//ul[@class='jobs-search__results-list']")
        for elemento in lista:
            itens =  elemento.find_elements_by_tag_name("li")
            for item in itens:
                nome = item.find_element_by_tag_name("h3")
                print("Vaga encontrada: %s" % nome.text)

bot = RoboEmprego()
#Passando parametro para buscar o tipo de emprego
bot.busca("financeiro",2)

