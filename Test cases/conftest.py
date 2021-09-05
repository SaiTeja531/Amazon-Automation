import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.maximize_window()

    driver.get("https://www.amazon.in/")
    wait = WebDriverWait(driver, 30)
    actions = ActionChains(driver)
    request.cls.actions = actions
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()
