from behave import given, when, then



@given(u'url as "{url}"')
def step_impl(context, url):
    context.orange = context.po.orangeLogin_page_init()
    context.orange.open(url)


@given(u'username as "{username}" and password as "{password}"')
def step_impl(context,username, password):
    print(username + password)
    context.orange.orangeLoginCreds(username, password)



@when(u'user clicks on login button')
def step_impl(context):
    context.orange.orangeLogin()


@then(u'the text "Dashboard" should be displayed')
def step_impl(context):
    context.orange.orangeValidation()

@then(u'logout from the application')
def step_impl(context):
    context.orange.orangeLogout()
    
