# SauceDemo: покупка товара с Playwright и PageObject

Пример UI-теста пользовательского пути покупки товара на [SauceDemo](https://www.saucedemo.com/).
Каждая страница вынесена в отдельный класс, общие действия собраны в `BasePage`.

## Требования

- Python 3.10 или новее
- Chromium для Playwright

## Установка и запуск

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest
```

В тесте используются демонстрационные учётные данные SauceDemo: `standard_user` / `secret_sauce`.
Адрес сайта задаётся фикстурой `base_url` в `conftest.py`.

## Структура проекта

```text
pages/
  base_page.py
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_information_page.py
  checkout_overview_page.py
  checkout_complete_page.py
tests/
  test_purchase.py
conftest.py
pytest.ini
requirements.txt
```
