from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.confirmation = page.locator(".complete-header")

    def confirmation_text(self) -> str:
        return self.confirmation.inner_text()
