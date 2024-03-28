from behave import given, when, then


@given(u'the application is loaded')
def open_login_url(context):
    context.saucedemo = context.po.sauceLogin_page_init()
    context.saucedemo.open()


@when(u'i see the application page')
def fill_login_page_field(context):
    context.saucedemo.sauceLoginLoad()


@then(u'the login page should be displayed')
def is_next_page(context):
    context.saucedemo.sauceLogin()