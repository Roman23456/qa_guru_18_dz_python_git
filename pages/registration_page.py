import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Open url")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step('Fill number')
    def fill_number(self, number):
        element = WebDriverWait(self.driver, timeout=15).until(
            EC.element_to_be_clickable((By.ID, "input-number"))
        )
        element.clear()
        element.send_keys(number)

    @allure.step('Fill Text')
    def fill_text(self, text):
        element = WebDriverWait(self.driver, timeout=15).until(
            EC.element_to_be_clickable((By.ID, "input-text"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step('Password')
    def fill_password(self, password):
        element = WebDriverWait(self.driver, timeout=15).until(
            EC.element_to_be_clickable((By.ID, "input-password"))
        )
        element.clear()
        element.send_keys(password)

    @allure.step('Fill date')
    def fill_date(self, date):
        element = WebDriverWait(self.driver, timeout=15).until(
            EC.element_to_be_clickable((By.ID, "input-date"))
        )
        element.clear()
        element.send_keys(date)

    @allure.step("Click Display Inputs button")
    def click_display_inputs(self):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.ID, "btn-display-inputs"))
        )
        element.click()