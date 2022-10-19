from selenium import webdriver
from selenium.webdriver import Chrome
from funcoes import *
#site -> http://quotes.toscrape.com/


driver = Chrome(executable_path='chromedriver.exe')

driver.get('http://quotes.toscrape.com/')

driver.maximize_window()

citacao_1 = coleta_citação(driver)
author_1 = coleta_autor(driver)
tags_1 = coleta_tags(driver)
print(citacao_1)
print(author_1)
print(tags_1)






