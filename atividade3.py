#!/usr/bin/python3
'''
ATIVIDADE: Objetivo passar alguma busca no YOUTUBE e o robo vai pesquisar e exibir as noticias sobre o tema procurado

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Firefox()

    def busca(self, busca, paginas):
        videos = []
        pagina =1
        url ="https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)

        while pagina <= paginas:
            titulos = self.webdriver.find_elements_by_xpath("//a[@id='video-title']")
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Vídeo encontrado: %s" % titulo.text) 
                    videos.append(titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print("Mundando para a página %s" % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scroll(0,%s);" % bottom)
        time.sleep(5)

bot = RoboYoutube()
bot.busca("bitcoin",10)
