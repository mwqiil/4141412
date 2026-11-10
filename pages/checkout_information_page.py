from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutInformationPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')

    def fill_information(
        self, first_name: str, last_name: str, postal_code: str
    ) -> CheckoutOverviewPage:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
        return CheckoutOverviewPage(self.page, self.base_url)
