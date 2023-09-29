from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("Launcging Chrome")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launcging FireFox")
    else:
        driver=webdriver.Edge()
        print("Launcging Dafult browser Microsoft Edge")
    #driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#pytest -v -s testCases/testLogin.py --browser chrome
#pytest -v -s -n=2 testCases/testLogin.py --browser chrome #parralel test run

# Pytest HTML Report
#It is a hook for adding environment info to html report
# def pytest_configure(config):
#     print("pytest_configure hook is running")
#     config._metadata = {
#         "Tester": "Amar",
#         "Project Name": "Hybrid Framework Practice",
#     }

metadata = {
    "Tester": "Amar",
    "Project Name": "Hybrid Framework Practice",
}
def pytest_metadata(metadata):
    metadata.update(metadata)

pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
