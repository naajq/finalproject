from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def price(sum_products, progucts_count, driver):         #Сверка нашей суммы без доставки
    bucket_price = 0
    for i in range(1, progucts_count + 1):
        price = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div[{i+1}]/div[2]/div[2]/div[2]"))).text
        price = int(price[0:3])
        bucket_price += price

    assert bucket_price == sum_products, "Итоговая цена на сайте и в корзине не сходятся!"
    print("\nЦены на странице и в корзине сходятся!")

    price_delivery = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[3]/div/div[1]/strong"))).text
    price_delivery = int(price_delivery[7:10])
    assert bucket_price + 140 == price_delivery
    print("\nЦена за доставку считается правильно!")                #Сверка нашей суммы + доставка установленная компанией