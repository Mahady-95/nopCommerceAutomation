# import time
# from pageObjects.LoginPage import LoginPage
# from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen
# from Utilities import XLUtls
#
# class Test002_DDTLogin:
#     baseUrl = ReadConfig.getApplicationURl()
#     path = ".//testData/data.xlsx"
#     logger = LogGen.loggen()
#
#     def test_LoginDDTTitle(self, setup):
#         self.logger.info("*********Test002_DDTLogin**********")
#         self.logger.info("*********Verifying DDt Login Test**********")
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = LoginPage(self.driver)
#
#         self.rows = XLUtls.getRowCount(self.path, 'Sheet1')
#         self.logger.info("Number of rows: %d", self.rows)
#
#         list_status = []
#
#         try:
#             for r in range(2, self.rows + 1):
#                 self.user = XLUtls.readData(self.path, 'Sheet1', r, 1)
#                 self.password = XLUtls.readData(self.path, 'Sheet1', r, 2)
#                 self.exp = XLUtls.readData(self.path, 'Sheet1', r, 3)
#
#                 self.lp.setUserName(self.user)
#                 self.lp.setPassword(self.password)
#                 self.lp.clickLogin()
#                 time.sleep(5)
#
#                 act_title = self.driver.title
#                 exp_title = "Dashboard / nopCommerce administration"
#
#                 if act_title == exp_title:
#                     if self.exp == "Pass":
#                         self.logger.info("***Passed***")
#                         list_status.append("Pass")
#                     elif self.exp == "Fail":
#                         self.logger.info("***Failed***")
#                         list_status.append("Fail")
#                 elif act_title != exp_title:
#                     print(act_title)
#                     print(exp_title)
#                     if self.exp == "Pass":
#                         self.logger.info("***Failed***")
#                         list_status.append("Fail")
#                     elif self.exp == "Fail":
#                         self.logger.info("***Passed***")
#                         list_status.append("Pass")
#         except Exception as e:
#             self.logger.error("An error occurred: %s", str(e))
#         # finally:
#         #     self.driver.quit()
#
#         if "Fail" not in list_status:
#             self.logger.info("***LoginDDT Test Passed***")
#             assert True
#         else:
#             self.logger.info("***LoginDDT Test Failed***")
#             assert False
#         self.logger.info("***End of LoginDDT Test***")
#         self.logger.info("***Completed TC_Login 002***")
#         self.driver.close()
#
#
#
#
#
#
#
#
#
import time

import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtls

class Test002_DDTLogin:
    baseUrl = ReadConfig.getApplicationURl()
    path = ".//testData/data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_LoginDDTTitle(self, setup):
        self.logger.info("*********Test002_DDTLogin**********")
        self.logger.info("*********Verifying DDt Login Test**********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtls.getRowCount(self.path, 'Sheet1')
        self.logger.info("Number of rows: %d", self.rows)

        list_status = []


        for r in range(2, self.rows + 1):
            self.user = XLUtls.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtls.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtls.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            time.sleep(5)
            self.driver.save_screenshot(".\\screenshots\\" + "test_LoginDDTPage.png")
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                print(act_title)
                print(exp_title)
                if self.exp == "Pass":
                    self.logger.info("***Failed***")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***Passed***")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("***LoginDDT Test Passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("***LoginDDT Test Failed***")
            self.driver.close()
            assert False
        self.logger.info("***End of LoginDDT Test***")
        self.logger.info("***Completed TC_Login 002***")










