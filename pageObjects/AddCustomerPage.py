import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_AddNew_xapth = "//a[normalize-space()='Add new']"
    txt_Email_xpath = "//input[@id='Email']"
    txt_Password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath= "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rd_MaleGender_xpath = "//label[normalize-space()='Male']"
    rd_FemaleGender_xpath = "//label[normalize-space()='Female']"
    txt_DOB_id = "DateOfBirth"
    txt_Company_name = "Company"
    checkbox_istaxempt_id = "IsTaxExempt"
    txt_Newsleter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_Item_Yourstore_xpath="//li[contains(text(),'Your store name')]"
    list_Item_Teststore2_xpath = "//li[contains(text(),'Test store 2')]"
    txt_CustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listItemAdministrator_xpath = "//li[contains(text(),'Administrators')]"
    listItemForumModerator_xpath = "//li[contains(text(),'Forum Moderators')]"
    listItemGuests_xpath = "//li[contains(text(),'Guests')]"
    listItemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listItemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOFVendor_xpath ="//select[@id='VendorId']"
    txt_Admincontent_xpath ="//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def clickCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.link_customer_submenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xapth).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)
    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH, self.listItemRegistered_xpath)
        elif role=='Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.listItemAdministrator_xpath)
        elif role=='Guests':
            time.sleep(3)
            dltregister_xpath="//span[@title='delete']"
            self.driver.find_element(By.XPATH, dltregister_xpath).click()
            self.listitem=self.driver.find_element(By.XPATH, self.listItemGuests_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH, self.listItemRegistered_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH, self.listItemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listItemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)
    def setManagerOfVendor(self, value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOFVendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH, self.rd_MaleGender_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH, self.rd_FemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_MaleGender_xpath).click()
    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.txt_DOB_id).send_keys(dob)

    def setCompanyName(self, comName):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(comName)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txt_Admincontent_xpath).send_keys(content)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()






