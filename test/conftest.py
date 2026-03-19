import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

from utils.attach import add_screenshot, add_page_source, add_console_logs, add_video


def pytest_addoption(parser):
    """Добавляем параметры командной строки"""
    parser.addoption("--test-number", action="store", default="1234356")

    parser.addoption("--test-text", action="store", default="wwwww")

    parser.addoption("--test-password", action="store", default="1234qj")

    parser.addoption("--test-date", action="store", default="10.08.1994")

    parser.addoption("--site-url", action="store", default=os.getenv("SITE_URL"),
                     help="URL тестируемого сайта")
    parser.addoption("--selenoid-url", action="store", default=os.getenv("SELENOID_URL"),
                     help="URL удаленного браузера (selenoid)")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер: chrome, firefox")
    parser.addoption("--browser-version", action="store", default="128.0",
                     help="Версия браузера")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Запуск в headless режиме")
    parser.addoption("--window-width", action="store", default="1920",
                     help="Ширина окна")
    parser.addoption("--window-height", action="store", default="1080",
                     help="Высота окна")


@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser-version")
    headless = request.config.getoption("--headless")
    window_width = request.config.getoption("--window-width")
    window_height = request.config.getoption("--window-height")
    selenoid_url = request.config.getoption("--selenoid-url")

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(f'--window-size={window_width},{window_height}')
    options.add_argument('--disable-blink-features=AutomationControlled')

    if headless:
        options.add_argument('--headless')

    selenoid_capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    yield driver

    add_screenshot(driver)
    add_page_source(driver)
    add_console_logs(driver)
    add_video(driver)

    driver.quit()