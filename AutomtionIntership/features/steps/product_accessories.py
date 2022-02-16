from behave import given, when, then


@given('Open GetTop page')
def open_page(context):
    context.app.main_page.open_main_page()


@when('Hover over accessories')
def hover_accessories(context):
    context.app.header.hover_accessories()


@then('Verify {expected_count} items are shown under accessories')
def verify_number_of_items(context, expected_count):
    context.app.header.verify_number_of_items(expected_count)


