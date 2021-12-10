#!/usr/bin/python3
'''
ATIVIDADE: Realizar uma busca de vagas no LINKEDIN passando um determinado tipo de função.
e realizando a busca nesse caso trazendo a descrição da vaga e salvando tudo em um arquivo
Referencia para ajudar na resolução:
https://pt.stackoverflow.com/questions/259769/abrir-e-fechar-v%C3%A1rias-abas-no-navegador-com-python

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RoboLinkedin():
    def __init__(self):
        self.webdriver = webdriver.Firefox()
    
    def busca (self, busca):

        arq = open("resultados-linkedin.txt", "w")
        url = "https://br.linkedin.com/jobs"
        self.webdriver.get(url)

        campo = self.webdriver.find_element_by_xpath("//input[@aria-label='Pesquisar cargos ou empresas']")
        campo.send_keys(busca)
        campo.send_keys(Keys.ENTER)
        time.sleep(3)

        lista = self.webdriver.find_elements_by_xpath("//ul[@class='jobs-search__results-list']")
        for elemento in lista:
            itens = elemento.find_elements_by_tag_name("li")
            for item in itens:
                nome = item.find_element_by_tag_name("h3")
                tempo = item.find_element_by_tag_name("time")
                url = item.find_element_by_tag_name("a").get_attribute("href")
                texto = "Vaga encontrada: %s - %s\n" % (nome.text, tempo.text)
                arq.write(texto)
                # Abre uma nova aba e vai para o site do SO
                self.webdriver.execute_script("window.open('%s', '_blank')" % url)
                # Muda de aba
                self.webdriver.switch_to.window(self.webdriver.window_handles[1])
                time.sleep(1)
                description = self.webdriver.find_element_by_xpath("//div[@class='show-more-less-html__markup show-more-less-html__markup--clamp-after-5']")
                arq.write("\n%s\n\n\n********************************************************************************************\n" % description.text)
                # Fecha a aba
                self.webdriver.close()
                #volta para a aba da pesquisa inicial
                self.webdriver.switch_to.window(self.webdriver.window_handles[0])
        arq.close()

bot = RoboLinkedin()
bot.busca("Blockchain")


