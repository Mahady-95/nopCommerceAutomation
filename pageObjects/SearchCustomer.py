from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_SearchEmail_xpath = "//input[@id='SearchEmail']"
    txt_searchFirstName_xpath = "//input[@id='SearchFirstName']"
    txt_searchLastName_xpath = "//input[@id='SearchLastName']"
    btn_search_xpath = "//button[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    table_Rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    def setSearchEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_SearchEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_SearchEmail_xpath).send_keys(email)
    def setSearchFirstName(self, sfname):
        self.driver.find_element(By.XPATH, self.txt_searchFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_searchFirstName_xpath).send_keys(sfname)

    def setSearchLastName(self, slname):
        self.driver.find_element(By.XPATH, self.txt_searchLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_searchLastName_xpath).send_keys(slname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Columns_xpath))
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.table_xpath)
            emailid=table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if Name == name:
                flag = True
                break
        return flag


