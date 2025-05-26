import pytest, os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qaguru_18_lesson_11.utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "127.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='127.0'
    )
@pytest.fixture(scope="session", autouse=True)
def setup_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def file_path():
    return os.path.join(os.path.dirname(__file__), 'files', 'meme.png')


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "goog:loggingPrefs": {"browser": "ALL"}
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    url = os.getenv('URL')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}/wd/hub",
        options=options)

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_logs(browser)

    browser.quit()
