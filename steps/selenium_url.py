from behave import *
from Common.CommonFunc.web_functions import go_to, get_current_url
import logging as logger
import Common.CommonSteps.common_steps



@then('current url should be {expected_url}')
def step_impl(context, expected_url):
    """
    :type context: behave.runner.Context
    """
    logger.info(f"{expected_url} - expected!!")
    get_url = get_current_url(context.driver)[:-1]
    logger.info(f"{get_url} returned!!")
    assert get_url == expected_url


