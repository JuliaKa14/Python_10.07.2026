# Lesson 10

## Описание проекта

Проект содержит автоматизированные UI-тесты, написанные с использованием паттерна **Page Object**.

В рамках проекта реализованы проверки:

- работы калькулятора;
- оформления заказа в интернет-магазине.

Для формирования отчета используется **Allure Framework**.

## Структура проекта
lesson_10/
│
├── pages/
│   ├── calculator_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── __init__.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_shop.py
│   └── __init__.py
│
├── requirements.txt
└── README.md

## Используемые технологии

- Python
- Selenium WebDriver
- Pytest
- Allure Framework

## Установка зависимостей

Установить необходимые библиотеки:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запустить все тесты:

```bash
pytest
```

Запустить тесты в подробном режиме:

```bash
pytest -v
```

## Формирование Allure-отчета

Для формирования результатов выполните команду:

```bash
pytest --alluredir=allure-results
```

## Просмотр Allure-отчета

Открыть отчет можно командой:

```bash
allure serve allure-results
```