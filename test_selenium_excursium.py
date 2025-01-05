import time

from conftest import driver
from locators import Locators

def test_auth_excursium(driver):
    driver.get('https://great-pascal.37-140-192-136.plesk.page/Client/Login')

    # Вводим email
    email = driver.find_element(*Locators.AUTH_EMAIL)
    email.send_keys('maximus7st@gmail.com')

    # Вводим пароль
    passw = driver.find_element(*Locators.AUTH_PASS)
    passw.send_keys('310906')

    # Нажимаем на кнопку входа в аккаунт
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(1)

    # Переход на страницу Все экскурсии
    logo = driver.find_element(*Locators.PICTURE_LOGO)
    logo.click()
    time.sleep(1)

    # Проверяем, что нас перенаправляет на список экскурсий после нажатия на поиск с пустым поиском
    button_search = driver.find_element(*Locators.BUTTON_SEARCH)
    button_search.click()
    time.sleep(1)

    assert driver.find_element(*Locators.TEXT_EXCURSIUM).text == "150+ экскурсий для школьников"