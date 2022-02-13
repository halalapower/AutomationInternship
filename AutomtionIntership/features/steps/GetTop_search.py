from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given("Open GetTop page")
def open_page(context):
    context.app.main_page.open_main_page
    raise NotImplementedError(u'STEP: Given Open Get-top page')


@when("Input product into Get-top search")
def step_impl(context):
    raise NotImplementedError(u'STEP: When Input product into Get-top search')


@when("Click on Get-top search icon")
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on Get-top search icon')


@then("Verify search worked")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify search worked')