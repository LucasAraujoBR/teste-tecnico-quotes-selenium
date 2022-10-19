# Para cada citação, os seguintes dados devem ser coletados:
# citação (string),
# autor (dictionary) com seu nome (string) e url da sua bio (string),
# tags (list).
import time
from selenium import webdriver


def coleta_citação(driver):
    time.sleep(3)
    citation = driver.find_element("xpath", '/html/body/div/div[2]/div[1]/div[1]/span[1]').get_attribute("innerText")
    return citation


def coleta_autor(driver):
    time.sleep(3)
    author = driver.find_element("xpath", '/html/body/div/div[2]/div[1]/div[1]/span[2]').get_attribute("innerText")
    return author

def coleta_tags(driver):
    time.sleep(3)
    tags = driver.find_element("xpath", '/html/body/div/div[2]/div[1]/div[1]/div').get_attribute("innerText")
    return tags