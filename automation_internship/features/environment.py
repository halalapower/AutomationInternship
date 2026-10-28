import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def browser_init(context):
    """Start the browser for a scenario.

    BROWSER=chrome|firefox (default chrome), HEADLESS=1 to run without a window.
    Selenium Manager (Selenium 4.6+) downloads the matching driver automatically.
    """
    browser = os.getenv('BROWSER', 'chrome').lower()
    headless = os.getenv('HEADLESS', '0') == '1'

    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('-headless')
        context.driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        options.add_argument('--window-size=1920,1080')
        context.driver = webdriver.Chrome(options=options)

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()
