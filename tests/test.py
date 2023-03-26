import time
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.bucket_page import Bucket_page
from pages.helper import price
from pages.login_page import Main_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Admin\\PycharmProjects\\resource\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)


def test_authorization():
    main = Main_page(driver)
    main.authorization()
    time.sleep(2)
    logging.info("Тест авторизации пройден!")


def test_select_product():
    main = Main_page(driver)
    main.click_shawerma()
    shawerma_1 = main.click_product_shawerma(1)
    time.sleep(2)
    shawerma_2 = main.click_product_shawerma(2)
    time.sleep(2)
    shawerma_3 = main.click_product_shawerma(3)
    time.sleep(2)

    main.click_burger()
    burger_1 = main.click_product_burger(1)
    time.sleep(2)

    main.click_bucket()
    bucket = Bucket_page(driver)
    bucket.delete_food(2)
    bucket.delete_food(3)
    price(sum_products=burger_1 + shawerma_2, progucts_count=2, driver=driver)
    logging.info("Тест покупки пройденf")


def test_input_info():
    bucket = Bucket_page(driver)
    bucket.input_name("Deni")
    bucket.input_number()
    bucket.input_adress()

    time.sleep(3)
    bucket.input_submission()
    bucket.accept_agreements()
    logging.info("Тест карзины пройден!")