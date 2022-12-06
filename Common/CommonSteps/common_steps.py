from behave import *
from Common.CommonFunc.web_functions import go_to, get_current_url
import logging as logger


@given('I go to {url}')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    logger.info(f"{url} being tested!!")
    context.driver = go_to(url)
