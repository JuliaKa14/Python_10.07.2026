from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/forms/post")

    # Сохраняем текущий URL

    current_url = driver.current_url

    # Находим поле ввода и вводим имя

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Ваше имя")

    # Находим кнопку Submit и нажимаем

    submit_button = driver.find_element(
        By.XPATH,
        "//button[text()='Submit order']"
    )
    submit_button.click()

    # Проверяем, что URL изменился

    assert driver.current_url != current_url

    driver.quit()
