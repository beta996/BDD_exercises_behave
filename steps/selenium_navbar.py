from behave import *
from selenium.common import NoSuchElementException

from Common.CommonFunc.web_functions import find_element
import logging as logger
import Common.CommonSteps.common_steps


@then('main navigation bar should be existing')
def step_impl(context):
    try:
        is_existing = find_element(context, "main_navbar")
    except NoSuchElementException('element not implemented!') as err:
        logger.error(err)
    return is_existing


@then('main navigation bar should be visible')
def step_impl(context):
    is_visible = find_element(context, "main_navbar").is_displayed()
    assert is_visible, True
