from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object страницы авторизации.
    """

    def __init__(self, driver) -> None:
        """
        Инициализирует страницу авторизации.

        :param driver: экземпляр WebDriver.
        :return: None.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: логин пользователя.
        :param password: пароль пользователя.
        :return: None.
        """
        self.driver.find_element(
            By.ID,
            "user-name"
        ).send_keys(username)

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()
