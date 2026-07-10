from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():

    driver = webdriver.Firefox()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()

    inventory.open_cart()

    cart.checkout()

    checkout.fill_form(
        "Иван",
        "Петров",
        "123456"
    )

    total = checkout.get_total()

    driver.quit()

    assert total == "Total: $58.29"
