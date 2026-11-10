from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_purchase_product(page, base_url: str) -> None:
    completion_page = (
        LoginPage(page, base_url)
        .open()
        .login("standard_user", "secret_sauce")
        .add_product_to_cart("Sauce Labs Backpack")
        .open_cart()
        .checkout()
        .fill_information("Alex", "Example", "12345")
        .finish_purchase()
    )

    expect(completion_page.confirmation).to_have_text("Thank you for your order!")
