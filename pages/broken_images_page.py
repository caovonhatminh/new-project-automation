from pages.base_page import BasePage
from utils.settings import BASE_URL


class BrokenImagesPage(BasePage):
    URL = f"{BASE_URL}/broken-images/"
    BROKEN_IMAGES = "//img[starts-with(@alt, 'Broken Image')]"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Broken Images")

    def get_broken_image_count(self) -> int:
        broken_images = self.page.locator(self.BROKEN_IMAGES).evaluate_all(
            """
            elements => elements.filter(
                element => element.naturalWidth === 0
            ).length
            """
        )
        return int(broken_images)
