import time
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.constants import MainPageItem, BucketPageItem


class Main_page(Base):

    url = 'https://nalchik.tiktak-delivery.ru/restaurant/burger-mania'
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Заходим на наш сайт, сверяем по значению Бургер Мания, так же делаем скриншот"""
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/h1")))
        x_1 = x.text
        assert x and x_1 == "Burger Mania", "Мы не зашли на сайт!"
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'

        self.driver.save_screenshot('C:\\Users\\Admin\\PycharmProjects\\finalproject\\screenshots\\' + name_screenshot)

    def click_burger(self):
        """
            Каталог Бургеры
        :return:
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, MainPageItem.BURGER)))
        x.click()
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, MainPageItem.BURGER_2)))
        x.click()

    def click_shawerma(self):
        """
            Каталог Шаурма
        :return:
        """
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, MainPageItem.SHAWERMA)))
        x.click()

    """Выбираем шаурму и отсекаем значения после нащей суммы (руб.)"""
    def click_product_shawerma(self, number):
        price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div[1]/div[{number}]/div/div[1]/div[1]"))).text
        price = int(price[0:3])

        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div[1]/div[{number}]/div/div[2]/div/button")))
        x.click()
        return price

    """Выбираем бургеры, и так же отсекаем значения"""
    def click_product_burger(self, number):
        price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div[1]/div[{number}]/div/div[1]/div[1]"))).text
        price = int(price[0:3])

        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div[1]/div[{number}]/div/div[2]/div/button")))
        x.click()
        time.sleep(2)
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button")))
        x.click()
        return price

    """Кликаем на нашу корзину"""
    def click_bucket(self):
        x = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, BucketPageItem.BUCKET)))
        x.click()

