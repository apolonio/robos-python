#!/usr/bin/python3
'''
ATIVIDADE: Acessar o FACEBOOK passando os parametro usuario e senha

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.facebook.com/login")


email = input("Seu email: ")
senha = input("Senha: ")

login = driver.find_element(By.XPATH,"//*[@id='email']")
login.send_keys(email)

login = driver.find_element(By.XPATH,"//*[@id='pass']")
login.send_keys(senha)

login.send_keys(Keys.ENTER)
