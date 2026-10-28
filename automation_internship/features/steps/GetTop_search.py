from behave import then, when

# Work in progress: the search scenario is tagged @wip and skipped by default.
# These steps still need a search-box page object (locator + submit + results check).


@when('Input product into Get-top search')
def input_product(context):
    raise NotImplementedError('TODO: add search box locator to MainPage and type the product name')


@when('Click on Get-top search icon')
def click_search_icon(context):
    raise NotImplementedError('TODO: add search icon locator to MainPage and click it')


@then('Verify search worked')
def verify_search(context):
    raise NotImplementedError('TODO: assert the results page lists the searched product')
