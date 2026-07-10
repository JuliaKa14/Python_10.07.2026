from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Page Object страницы товаров.
    """

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу товаров.

        :param driver: экземпляр WebDriver.
        :return: None.
        """
        self.driver = driver

    def add_backpack(self) -> None:
        """
        Добавляет товар Sauce Labs Backpack в корзину.

        :return: None.
        """
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_tshirt(self) -> None:
        """
        Добавляет товар Sauce Labs Bolt T-Shirt в корзину.

        :return: None.
        """
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self) -> None:
        """
        Добавляет товар Sauce Labs Onesie в корзину.

        :return: None.
        """
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-onesie"
        ).click()

    def open_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None.
        """
        self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()
