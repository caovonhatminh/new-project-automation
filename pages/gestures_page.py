from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.settings import BASE_URL


class GesturesPage(BasePage):
    URL = f"{BASE_URL}/gestures/"
    MOVEABLE_BOX = "//div[@id='moveMe']"
    MOVEABLE_BOX_HEADER = "//div[@id='moveMeHeader']"
    DRAG_IMAGE = "//div[@id='div1']//img[@id='dragMe']"
    FIRST_DROPZONE_IMAGE = "//div[@id='div1']//img[@id='dragMe']"
    SECOND_DROPZONE = "//div[@id='div2']"
    SECOND_DROPZONE_IMAGE = "//div[@id='div2']//img[@id='dragMe']"

    def open_page(self) -> None:
        self.open(self.URL)

    def verify_page_loaded(self) -> None:
        self.expect_heading("Gestures")

    def verify_drag_source_present(self) -> None:
        drag_source = self.page.locator(self.DRAG_IMAGE)
        expect(drag_source).to_be_visible()

    def verify_drop_target_present(self) -> None:
        drop_target = self.page.locator(self.SECOND_DROPZONE)
        expect(drop_target).to_be_visible()

    def drag_moveable_box(self) -> tuple[float, float]:
        moveable_box = self.page.locator(self.MOVEABLE_BOX)
        box_before = moveable_box.bounding_box()
        assert box_before is not None

        moveable_box_header = self.page.locator(self.MOVEABLE_BOX_HEADER)
        moveable_box_header.hover()
        self.page.mouse.down()
        self.page.mouse.move(box_before["x"] + 120, box_before["y"] + 80)
        self.page.mouse.up()

        box_after = moveable_box.bounding_box()
        assert box_after is not None
        return box_before["x"], box_after["x"]

    def drag_image_to_second_box(self) -> tuple[int, int]:
        drag_image = self.page.locator(self.DRAG_IMAGE)
        second_dropzone = self.page.locator(self.SECOND_DROPZONE)
        first_dropzone_image = self.page.locator(self.FIRST_DROPZONE_IMAGE)
        second_dropzone_image = self.page.locator(self.SECOND_DROPZONE_IMAGE)

        drag_image.drag_to(second_dropzone)
        return first_dropzone_image.count(), second_dropzone_image.count()
