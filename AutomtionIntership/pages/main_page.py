from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



class MainPage(Page):
    IMG = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2013/08/mc13-1-1536x1510-1-300x300.jpg']")
    QUICK_VIEW = (By.CSS_SELECTOR, "a.quick-view.quick-view-added")
    CLOSE_QUICK_VIEW = (By.XPATH, "//button[@class='mfp-close']")
    CART = (By.XPATH, "//button[@class='single_add_to_cart_button button alt']")
    PRODUCT_CART = (By.CSS_SELECTOR, "span.cart-icon.image-icon strong")
    LEFT_ARROW = (By.CSS_SELECTOR, "div.hide-for-off-canvas li.prod-dropdown.has-dropdown "
                                   "a.button.icon.is-outline.circle")
    RIGHT_ARROW = (By.XPATH, "//div[@class='hide-for-off-canvas']//li[@class='prod-dropdown has-dropdown']")
    HOME_BUTTON = (By.XPATH, "//a[@href='https://gettop.us/']")


    def open_main_page(self):
        self.open_page()

    def hover_image(self):
        image = self.find_element(*self.IMG)
        actions = ActionChains(self.driver)
        actions.move_to_element(image)
        actions.perform()

    def quick_view(self):
        self.click(*self.QUICK_VIEW)

    def close_quick_view(self):
        self.click(*self.CLOSE_QUICK_VIEW)

    def add_to_cart(self):
        self.click(*self.CART)

    def verify_product_in_cart(self):
        self.verify_text('1', *self.PRODUCT_CART)

    def click_product(self):
        self.click(*self.IMG)

    def click_left_arrow(self):
        self.click(*self.LEFT_ARROW)

    def click_right_arrow(self):
        self.click(*self.RIGHT_ARROW)

    def click_home_button(self):
        self.click(*self.HOME_BUTTON)
