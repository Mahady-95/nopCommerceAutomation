import time

import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test001Login:
    baseUrl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPasssword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        act_title = self.driver.title
        time.sleep(3)
        if act_title == "Your store. Login":
            assert True
            #self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.logger.info("*********HomePage or Login page**********")
            self.driver.close()
        else:
            #self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
        time.sleep(5)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginTitle(self, setup):
        self.logger.info("*********Test001Login**********")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        self.logger.info("*********Login successful**********")
        #self.driver.save_screenshot(".\\screenshots\\" + "test_LoginTitle.png")
        time.sleep(5)
        self.driver.close()
        self.logger.info("*********Test001Login PASSED YEAH**********")


