import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage





class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPasssword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddCustomer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("********* Login successful **********")

        self.logger.info("******* Starting Add Customer Page ******")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickCustomerMenu()
        time.sleep(3)
        self.addcust.clickCustomerSubMenu()
        time.sleep(3)
        self.addcust.clickOnAddNew()
        time.sleep(3)

        self.logger.info("******* Providing Customer Details ********")

        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        time.sleep(3)
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDOB("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing..............")
        self.addcust.clickSave()
        time.sleep(10)

        self.logger.info("******* Saving Customer Details ********")

        self.logger.info("******* Add Customer Validation Started ********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******* Add Customer Test Passed ********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("******* Add Customer Test Failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("******* Ending Add Customer Test********")

def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
            return ''.join(random.choice(chars) for x in range(size))


#pytest -s -v --html=reports\report.html testCases/test_AddCustomer.py --browser chrome


