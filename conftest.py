import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """Адрес тестируемого магазина; передаётся страницам через конструкторы."""
    return "https://www.saucedemo.com/"
