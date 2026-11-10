from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.cart_link = page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_name: str) -> "InventoryPage":
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product.locator("button.btn_inventory").click()
        return self

    def open_cart(self) -> CartPage:
        self.cart_link.click()
        return CartPage(self.page, self.base_url)
