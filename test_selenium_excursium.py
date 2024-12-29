import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    #driver.get('https://great-pascal.37-140-192-136.plesk.page/Client/Login')
    time.sleep(2)

    yield driver

    driver.quit()
def test_auth_excursium(driver):
    driver.get('https://great-pascal.37-140-192-136.plesk.page/Client/Login')
    # Вводим email
    driver.find_element(By.XPATH, '//*[@id="login-vue"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]').send_keys('maximus7st@gmail.com')
    # Вводим парол
    driver.find_element(By.XPATH, '//*[@id="login-vue"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]').send_keys('310906')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'login-btn').click()
    time.sleep(10)
    # Ввод подтверждающего кода в ручном режиме, так как он приходит на почту
    driver.find_element(By.CSS_SELECTOR, 'button#checkCode-btn').click()
    time.sleep(20)
    # Переход на страницу Все экскурсии
    driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul[1]/li[1]/a[1]').click()
    time.sleep(5)
    driver.find_element(By. XPATH, '//*[@id="profileDropdown"]/img[1]').click()
    time.sleep(5)
    driver.find_element(By. CSS_SELECTOR, 'html > body > header > nav > div > ul > li:nth-of-type(4) > ul > li:nth-of-type(4) > a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logo-normal"]').click()
    time.sleep(3)
    # Проверяем что нас перенаправляет на список экскурсий после нажатия на поиск с пустым поиском
    driver.find_element(By.CSS_SELECTOR, 'a#searchLink').click()
    time.sleep(3)


