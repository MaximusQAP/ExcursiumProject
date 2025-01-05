from selenium.webdriver.common.by import By

class Locators(object):
    AUTH_EMAIL = (By.XPATH, './/*[@id="login-vue"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]')
    AUTH_PASS = (By.XPATH, './/*[@id="login-vue"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="navbarCollapse"]/ul[1]/li[1]/a[1]')
    PICTURE_LOGO = (By.XPATH, '//*[@id="logo-normal"]')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'a#searchLink')
    TEXT_EXCURSIUM = (By.TAG_NAME, 'h1')