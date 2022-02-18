from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ..pages.base_page import Page
from time import sleep


class MainPage(Page):
    TOP_BANNER = (By.CSS_SELECTOR, '.header_logo')
    RIGHT_ARROW = (By.CSS_SELECTOR, 'button[aria-label="Next"] svg.flickity-button-icon path.arrow')
    LEFT_ARROW = (By.CSS_SELECTOR, 'button[aria-label="Previous"] svg.flickity-button-icon path.arrow')
    RIGHT_DOT = (By.CSS_SELECTOR, 'li[aria-label="Page dot 2"]')
    LEFT_DOT = (By.CSS_SELECTOR, 'li[aria-label="Page dot 1"]')
    NEXT_PRODUCT_NAME = (By.XPATH, '//div[@class="text-inner text-center"]//strong[contains(text(), "Mac")]')
    FIRST_PRODUCT_NAME = (By.XPATH, '//div[@class="text-inner text-left"]//strong[contains(text(), "iPad")]')
    NEXT_PRODUCT = ''
    FIRST_PRODUCT = ''
    LOGO = (By.CSS_SELECTOR, 'div#logo a[href]')

    def open_main_page(self):
        self.open_page()

    def hover_over_top_banner(self):
        banner = self.find_element(*self.TOP_BANNER)
        actions = ActionChains(self.driver)
        actions.move_to_element(banner)
        actions.perform()

    def Click_the_right_arrow_icon(self):
        self.wait_for_element_click(*self.RIGHT_ARROW)
        sleep(5)

    def Click_the_left_arrow_icon(self):
        self.wait_for_element_click(*self.LEFT_ARROW)
        sleep(5)

    def Click_right_dot(self):
        self.wait_for_element_click(*self.RIGHT_DOT)
        sleep(5)

    def Click_left_dot(self):
        self.wait_for_element_click(*self.LEFT_DOT)
        sleep(5)

    def store_next_page_product_name(self):
        self.NEXT_PRODUCT = self.find_element(*self.NEXT_PRODUCT_NAME).text
        print(f'next product name is {self.NEXT_PRODUCT}')

    def store_first_product_name(self):
        self.FIRST_PRODUCT = self.find_element(*self.FIRST_PRODUCT_NAME).text
        print(f'first product name is {self.FIRST_PRODUCT}')

    def verify_product_text(self):
        assert self.FIRST_PRODUCT != self.NEXT_PRODUCT, f'Error! Actual {self.FIRST_PRODUCT} does not differ from ' \
                                                        f'Expected{self.NEXT_PRODUCT} '
