from behave import then


@then("Click_and_verify_product")
def Click_and_verify_product(context):
    context.app.product_page.click_and_verify_product()
