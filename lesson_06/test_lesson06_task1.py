from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # Открываем страницу

    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/2"
    )

    # Находим кнопку Start

    start_button = driver.find_element(
        By.CSS_SELECTOR,
        "#start button"
    )

    # Нажимаем кнопку

    start_button.click()

    # Ждём появления текста

    wait = WebDriverWait(driver, 10)

    hello_text = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "finish")
        )
    )

    # Делаем скриншот

    driver.save_screenshot("dynamic_loading.png")

    # Проверяем текст

    assert hello_text.text == "Hello World!"

    driver.quit()
