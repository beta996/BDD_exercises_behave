from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service



def go_to(url):
    """
    :param:  the url to navigate to
    :return: driver instance
    """
    options = Options()
    options.binary_location = r'C:\Program Files\WindowsApps\Mozilla.Firefox_107.0.1.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe'
    # driver = webdriver.Firefox(executable_path=r'C:\Users\bjackowska3\Downloads\geckodriver-v0.32.0-win64')
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    url = url.strip()
    driver.get(url)

    return driver


def get_current_url(driver):
    return str(driver.current_url)


def find_element(context, element, locator):
    if locator.lower() == 'id':
        element_found = context.driver.find_element(By.ID, element)
    elif locator.lower() == 'name':
        element_found = context.driver.find_element(By.NAME, element)
    else:
        raise Exception('Locator not known!')
    return element_found

def input_text(context, element, text):
    element.send_keys(text)

def click_element(context, element):
    element.click()

if __name__ == '__main__':
    go_to('https://www.selenium.dev')