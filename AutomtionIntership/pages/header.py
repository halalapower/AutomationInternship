from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from ..pages.base_page import Page


class Header(Page):

    HOVER_ACCESSORIES = (By.ID, '#menu-item-472')
    NUMBER_OF_ACCESSORIES = (By.CSS_SELECTOR, '#menu-item-472 a')

    def hover_accessories(self):
        flag = self.find_element(*self.HOVER_ACCESSORIES)
        action = ActionChains(self.driver)
        action.move_to_element(flag)
        action.perform()

    def verify_number_of_items(self, expected_count):
        actual_count = len(self.find_elements(*self.HOVER_ACCESSORIES))
        assert int(expected_count) == actual_count, f'Actual {actual_count} does not match expected {expected_count}'

    def click_accessories(self):
        self.click(*self.HOVER_ACCESSORIES)