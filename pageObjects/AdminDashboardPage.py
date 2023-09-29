from selenium.webdriver.common.by import By


class AdmindashBoardPage:
    link_admin_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]"


    def __init__(self, driver):
        self.driver = driver

    def clickAdmin(self):
        self.driver.find_element(By.XPATH, self.link_admin_xpath).click()