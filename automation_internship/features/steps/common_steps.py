from behave import given


@given('Open GetTop page')
def open_page(context):
    context.app.main_page.open_main_page()
