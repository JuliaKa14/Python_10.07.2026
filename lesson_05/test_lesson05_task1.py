from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():

    # Открываем главную страницу

    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")

    # Сохраняем исходный URL

    main_url = driver.current_url

    # Находим и кликаем ссылку HTML form

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    html_form_link.click()

    assert driver.current_url == "https://httpbin.org/forms/post"

    driver.back()

    assert driver.current_url == main_url

    driver.quit()
