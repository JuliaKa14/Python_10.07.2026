import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description(
    "Проверяем авторизацию пользователя, добавление товаров "
    "в корзину и итоговую стоимость заказа."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """
    Тест проверяет полный сценарий оформления заказа.
    """

    driver = webdriver.Firefox()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открываем страницу авторизации"):
        login.open()

    with allure.step("Авторизуемся под пользователем standard_user"):
        login.login(
            "standard_user",
            "secret_sauce"
        )

    with allure.step("Добавляем товары в корзину"):
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()

    with allure.step("Переходим в корзину"):
        inventory.open_cart()

    with allure.step("Нажимаем кнопку Checkout"):
        cart.checkout()

    with allure.step("Заполняем форму оформления заказа"):
        checkout.fill_form(
            "Иван",
            "Петров",
            "123456"
        )

    with allure.step("Получаем итоговую стоимость заказа"):
        total = checkout.get_total()

    with allure.step("Проверяем итоговую стоимость"):
        assert total == "Total: $58.29"

    driver.quit()
