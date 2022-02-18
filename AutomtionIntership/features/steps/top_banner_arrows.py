from behave import given, when, then


@given('Open GetTop page')
def open_page(context):
    context.app.main_page.open_main_page()


@when('Hover over top banner')
def hover_over_top_banner(context):
    context.app.main_page.hover_over_top_banner()


@then('Click the right arrow icon')
def Click_the_right_arrow_icon(context):
    context.app.main_page.Click_the_right_arrow_icon()


@then('Click the left arrow icon')
def Click_the_left_arrow_icon(context):
    context.app.main_page.Click_the_right_arrow_icon()


@then('Click the bottom right dot')
def Click_right_dot(context):
    context.app.main_page.Click_right_dot()


@then('Click the bottom left dot')
def Click_left_dot(context):
    context.app.main_page.Click_left_dot()


@then('Store next page product name')
def store_next_page_product_name(context):
    context.app.main_page.store_next_page_product_name()


@then('store first page product name')
def store_first_product_name(context):
    context.app.main_page.store_first_product_name()


@then('verify different products are available')
def verify_product_text(context):
    context.app.main_page.verify_product_text()
