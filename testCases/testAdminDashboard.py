import time

from pageObjects.AdminDashboardPage import AdmindashBoardPage
from pageObjects.LoginPage import LoginPage


class Test002AdminDashboard():
    baseUrl = "https://sqa.deepchainlabs.com/login"
    username = "admindcl@gmail.com"
    password = "adminpassword"

    def testAdminDashboard(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(5)

        self.dash=AdmindashBoardPage(self.driver)
        self.dash.clickAdmin()
        print("DashBoard")

        time.sleep(5)
        self.driver.close()



