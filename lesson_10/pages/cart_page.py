from selenium.webdriver.common.by import By


class CartPage:
    """
    Page Object страницы корзины.
    """

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: экземпляр WebDriver.
        :return: None.
        """
        self.driver = driver

    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout для перехода
        к оформлению заказа.

        :return: None.
        """
        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()
