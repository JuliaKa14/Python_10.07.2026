import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверяем, что калькулятор выполняет сложение "
    "чисел 7 и 8 с задержкой 45 секунд"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
def test_calculator():
    """
    Тест проверяет работу страницы калькулятора.
    """

    driver = webdriver.Chrome()

    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажимаем кнопку 7"):
        page.click_button("7")

    with allure.step("Нажимаем кнопку сложения"):
        page.click_button("+")

    with allure.step("Нажимаем кнопку 8"):
        page.click_button("8")

    with allure.step("Нажимаем кнопку равно"):
        page.click_button("=")

    with allure.step("Проверяем, что результат вычисления отображается"):
        assert page.get_result() == "15"

    driver.quit()
