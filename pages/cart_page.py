from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.checkout_information_page import CheckoutInformationPage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.checkout_button = page.locator('[data-test="checkout"]')

    def checkout(self) -> CheckoutInformationPage:
        self.checkout_button.click()
        return CheckoutInformationPage(self.page, self.base_url)
