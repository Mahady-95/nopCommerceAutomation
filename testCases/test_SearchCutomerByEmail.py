import time

import pytest

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer


class Test_004_SearchCustomer:
    baseUrl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPasssword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCutomer(self,setup):
        self.logger.info("***** Test_004_SearchCustomer *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("********* Login successful **********")

        self.logger.info("******* Starting Search Customer Page ******")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickCustomerMenu()
        time.sleep(3)
        self.addcust.clickCustomerSubMenu()
        time.sleep(3)

        self.logger.info("*******  Searching Customer By Email ******")

        searchcust = SearchCustomer(self.driver)
        searchcust.setSearchEmail("admin@yourStore.com")
        searchcust.clickSearch()

        time.sleep(5)
        status = searchcust.searchCustomerByEmail("admin@yourStore.com")
        assert True == status
        time.sleep(5)
        self.logger.info("******* Test_004_SearchCustomer Finished********")
        self.driver.close()

#pytest -s -v --html=reports\report.html testCases/test_SearchCutomerByEmail.py --browser chrome


