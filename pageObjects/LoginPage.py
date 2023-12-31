from selenium.webdriver.common.by import By
class LoginPage:
    text_username_id = "Email"
    text_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()