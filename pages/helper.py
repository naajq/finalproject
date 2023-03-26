from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def price(sum_products, progucts_count, driver):
    """
        Сверяет цены
    :param sum_products: Сумма выбранных нами товаров, указывается явно в тесте
    :param progucts_count: Количество товаров в карзине, указывается явно в тесте
    :param driver: Драйвер братик
    """
    "Перебираем товары в корзине и записываем в общуюю сумму bucket_price"
    bucket_price = 0
    for i in range(1, progucts_count + 1):
        price = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div[{i+1}]/div[2]/div[2]/div[2]"))).text
        price = int(price[0:3])
        bucket_price += price

    "Сверяем цену товаров в корзине с sum_products"
    assert bucket_price == sum_products, "Итоговая цена на сайте и в корзине не сходятся!"
    print("\nЦены на странице и в корзине сходятся!")

    "Проверяем итоговую цену с доставкой"
    price_delivery = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[3]/div/div[1]/strong"))).text
    price_delivery = int(price_delivery[7:10])
    assert bucket_price + 140 == price_delivery
    print("\n Цена за доставку считается правильно!")