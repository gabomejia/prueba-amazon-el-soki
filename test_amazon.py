import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

def test_direccion_by_class():

    load_dotenv('.env')

    mail = os.getenv("MAIL")
    password = os.getenv('PASSWORD')
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/')

    Identificador = driver.find_element(By.ID, 'nav-link-accountList')
    Identificador.click()
    driver.find_element(By.ID, 'ap_email').send_keys(mail, Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.NAME, 'password').send_keys(password, Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.ID, 'nav-global-location-popover-link').click()
    time.sleep(3)


    # if region
    # pass

# test_direccion_by_class()