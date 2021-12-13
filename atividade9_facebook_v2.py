#!/usr/bin/python3
'''
ATIVIDADE: 

'''
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

usr=input('Enter Email Id:')
pwd=input('Enter Password:')

#driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')

print ("Opened facebook")
driver.implicitly_wait(3)


user = driver.find_element_by_id('email')
user.send_keys(usr)
driver.implicitly_wait(3)

senha = driver.find_element_by_id('pass')
senha.send_keys(pwd)
driver.implicitly_wait(3)

login = driver.find_element_by_id('loginbutton')
login.click()
