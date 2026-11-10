from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.finish_button = page.locator('[data-test="finish"]')

    def finish_purchase(self) -> CheckoutCompletePage:
        self.finish_button.click()
        return CheckoutCompletePage(self.page, self.base_url)
