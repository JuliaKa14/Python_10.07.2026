from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://gitflic.ru")

input("Войдите в аккаунт вручную, затем нажмите Enter...")

print(driver.get_cookies())

driver.quit()
