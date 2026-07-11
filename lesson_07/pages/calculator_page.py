from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay):
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(delay)

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        ).click()

    def get_result(self):
        return WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                "15"
            )
        )
