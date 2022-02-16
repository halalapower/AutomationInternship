from selenium.webdriver.common.by import By
from ..pages.base_page import Page


class ProductPage(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title')
    TOTAL_ACCESSORIES = (By.CSS_SELECTOR, '#menu-item-472 a')

    def click_and_verify_product(self):
        expected_text = ['Cases & protection', 'AirPods with Wireless Charging Case', 'AirPods Pro']
        total = self.find_elements(*self.TOTAL_ACCESSORIES)
        for i in range(len(total)):
            link = self.find_elements(By.CSS_SELECTOR, '#menu-item-472 a')[i]
            link.click()
            actual_text = self.find_element(*self.PRODUCT_TITLE).text
            assert expected_text[i] == actual_text, f'Actual text {actual_text} /' \
                                                    f'does not match Expected text {expected_text} '
