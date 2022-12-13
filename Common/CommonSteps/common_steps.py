from behave import *
from Common.CommonFunc.web_functions import go_to, get_current_url
import logging as logger
from frontend_testing.config import URLCONFIG

@given('I go to {url}')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    url = URLCONFIG.get(url)
    url = URLCONFIG.get('base') + url
    logger.info(f"{url} being tested!!")
    context.driver = go_to(url.strip())
