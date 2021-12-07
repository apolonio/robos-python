#!/usr/bin/python3
'''
ATIVIDADE: Realizar uma busca no dominio REGISTRO.BR e verficiar se os domoinios passados na lista estao disponiveis para registro.
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#BIBLIOTECA PARA TRABALHAR COME EXCEL
#import xlrd
#from xlrd import sheet

print("Iniciando a busca dos domínios .....\n")
arq = open("resultado_registro.txt","w")
#dominios = []

#workbook = xlrd.open_workbook("dominios.ods")
#sheet = workbook.sheet_by_index(0)

dominios=["www.icriacoes.com.br", "www.manualcripto.com.br","www.criptoflix.com.br","www.escom.eb.mil.br"]

print("Achou ...\n")

'''
for linha in range(0,6):
    dominios.append(sheet.cell_value(linha,0))
'''

driver = webdriver.Firefox()
driver.maximize_window()    # aumentar tela
driver.implicitly_wait(20)  # segurar a pesquisa
driver.get("https://registro.br/")


for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()

    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    resultados = driver.find_elements_by_tag_name("strong")
    texto = ("Dominio %s %s\n" % (dominio, resultados[4].text))

    arq.write(texto)

arq.close()
