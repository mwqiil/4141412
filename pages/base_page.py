from typing import TypeVar

from playwright.sync_api import Page


PageType = TypeVar("PageType", bound="BasePage")


class BasePage:
    """Общие для страниц действия и доступ к Playwright Page."""

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self: PageType, path: str = "") -> PageType:
        self.page.goto(f"{self.base_url}/{path.lstrip('/')}")
        return self

    def title(self) -> str:
        return self.page.title()
