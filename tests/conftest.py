import pytest
from datetime import date
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from ui_testing.model.pages.practice_form import PracticePage
from ui_testing.utils import attach
from ui_testing.model.data.user import User


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="function")
def user():
    return User(
        first_name='Chev',
        last_name='Chelios',
        email='ChevChelios@gmail.com',
        phone='1234567890',
        address='Moscow',
        birthday=date(1989, 10, 12),
        gender='Male',
        subject='Economics',
        hobbies='Music',
        image='1.png',
        state='NCR',
        city='Delhi'
    )


@pytest.fixture(scope="function")
def practice_form():
    return PracticePage()

