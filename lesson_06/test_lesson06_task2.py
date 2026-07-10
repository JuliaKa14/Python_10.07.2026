from selenium import webdriver
from cookies import cookies_user1, cookies_user2


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru")

    # Авторизация первым пользователем

    for cookie in cookies_user1:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/junissta")

    url_user1 = driver.current_url

    # Выход (очистка cookie)

    driver.delete_all_cookies()
    driver.refresh()

    # Авторизация вторым пользователем

    for cookie in cookies_user2:
        driver.add_cookie(cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/julianka")

    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
