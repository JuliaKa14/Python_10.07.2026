from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    # Добавляем товары в корзину
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    ).click()

    # Переходим в корзину
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Checkout
    driver.find_element(
        By.ID,
        "checkout"
    ).click()

    # Заполняем форму
    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Иван")

    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys("Петров")

    driver.find_element(
        By.ID,
        "postal-code"
    ).send_keys("123456")

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    # Получаем итоговую стоимость
    total = driver.find_element(
        By.CLASS_NAME,
        "summary_total_label"
    ).text

    driver.quit()

    assert total == "Total: $58.29"
