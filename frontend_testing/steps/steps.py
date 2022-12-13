import Common.CommonSteps.common_steps
from behave import when, given, then, step
from Common.CommonFunc import web_functions
from frontend_testing import config

@when("I type {email} into username form")
def step_impl(context, email):
    """
    :param email: emai being tested
    :type context: behave.runner.Context
    """
    element = config.ELEMENTCONFIG.get('username_form')
    found_element = web_functions.find_element(context, element, 'id')
    web_functions.input_text(context, found_element, email)


@step("I type {psswrd} into password form")
def step_impl(context, psswrd):
    """
    :type psswrd: str
    :param psswrd: password being tested
    :type context: behave.runner.Context
    """
    element = config.ELEMENTCONFIG.get('password_form')
    found_element = web_functions.find_element(context, element, 'id')
    web_functions.input_text(context, found_element, psswrd)


@step("I click login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = config.ELEMENTCONFIG.get('login_btn')
    found_element = web_functions.find_element(context, element, 'name')
    web_functions.click_element(context, found_element)
