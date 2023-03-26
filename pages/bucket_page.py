import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

"""Наша финальная страница покупки, вводим значения в поля, доходим до оплаты, и делаем скриншот для подтверждения"""
class Bucket_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def delete_food(self, number):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div[{number}]/div[2]/div[2]/div[3]/a")))
        x.click()

    def input_name(self, name):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input']")))
        x.send_keys(name)

    def input_number(self):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input js_phone-mask']")))
        x.send_keys("9930010707")

    def input_adress(self):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input frame__input js-frame__input js-delivery-address']")))
        x.send_keys("Тарчокова, 21к1")
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[1]/div[5]/div/div[1]/div/a[1]")))
        x.click()

    def input_submission(self):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "change")))
        x.send_keys("5000")

    def accept_agreements(self):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='form__checkbox--label']")))
        x.click()
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'

        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\finalproject\\screenshots\\' + name_screenshot)