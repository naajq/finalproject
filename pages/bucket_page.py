import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Bucket_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def delete_food(self, number):
        """
            Удаление товара из карзины
        :param number: Номер товара
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div[{number}]/div[2]/div[2]/div[3]/a")))
        x.click()

    def input_name(self, name):
        """
            Ввод поля "Name"
        :param name: Имя
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input']")))
        x.send_keys(name)

    def input_number(self):
        """
            Ввод поля "Number"
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input js_phone-mask']")))
        x.send_keys("9930010707")

    def input_adress(self):
        """
            Ввод поля "Adress"
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form__input frame__input js-frame__input js-delivery-address']")))
        x.send_keys("Тарчокова, 21к1")
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[1]/div[5]/div/div[1]/div/a[1]")))
        x.click()

    def input_submission(self):
        """
            Ввод поля "Change"
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "change")))
        x.send_keys("5000")

    def accept_agreements(self):
        """
            Согласие с политикой сайта
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='form__checkbox--label']")))
        x.click()
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'

        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\finalproject\\screenshots\\' + name_screenshot)