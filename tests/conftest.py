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

    driver.implicitly_wait(20)
    driver.get("http://localhost:8000")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()

# Fixture untuk mengambil screenshot jika terjadi kegagalan
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to capture screenshots when a test fails and embed them in the pytest HTML report.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when == "call" or report.when == "setup":
        # Ambil driver dari fixture request
        driver = getattr(item.instance, "driver", None)
        if report.failed and driver:
            # Pastikan folder untuk menyimpan screenshot dibuat
            current_dir = os.getcwd()
            report_dir = os.path.join(current_dir, "screenshots")
            os.makedirs(report_dir, exist_ok=True)

            # Nama file screenshot
            sanitized_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            screenshot_path = os.path.join(report_dir, f"{sanitized_name}.png")

            # Ambil screenshot
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot diambil: {screenshot_path}")

            # Ambil plugin pytest-html
            pytest_html = item.config.pluginmanager.getplugin("html")

            # Tambahkan screenshot ke laporan HTML
            if pytest_html:
                relative_path = f"./../../screenshots/{sanitized_name}.png"
                html = (
                    f'<div><img src="{relative_path}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

    report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

