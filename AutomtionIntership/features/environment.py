from ..app.application import Application
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path="/Users/labzizihind/python-selenium-automation/chromedriver")
    # context.browser = webdriver.Safari() context.browser = webdriver.Firefox(
    # executable_path="/Users/labzizihind/PycharmProjects/AutomationInternship/geckodriver")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

    # HEADLESS MODE#
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(executable_path="/Users/labzizihind/PycharmProjects/AutomationInternship"
                                                      "/AutomtionIntership/chromedriver", chrome_options=options)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
