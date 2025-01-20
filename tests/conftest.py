import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")

    if browser_name =="chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name=="firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser_name=="edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(10)
    driver.get("http://localhost:8000")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            # _capture_screenshot(file_name)

            current_dir = os.getcwd()
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

            # Define the report directory as "newreports" in the parent directory
            report_dir = os.path.join(parent_dir, "newreports", "screenshots")
            os.makedirs(report_dir, exist_ok=True)  # Ensure the directory exists

            # Define the screenshot file name and normalize it
            sanitized_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            file_name = os.path.join(report_dir, sanitized_name + ".png")

            # Capture the screenshot
            _capture_screenshot(file_name)

            if file_name:
                # relative_path = os.path.relpath(file_name, start=report_dir)
                # relative_path = os.path.relpath(file_name, start=os.path.dirname(item.config.option.htmlpath))
                sanitized_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
                relative_path = os.path.join("screenshots", sanitized_name + ".png")
                print("relative_path= ", relative_path)
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % relative_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

