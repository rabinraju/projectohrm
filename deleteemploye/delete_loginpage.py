from selenium.webdriver.common.by import By


class delete:
    def __init__(self, driver):
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    login_button_locator = "//form/div[3]/button"
    pim_button_locator = "//span[text()='PIM']"
    click_delete_locator = "//i[@class='oxd-icon bi-trash'][1]"
    sure_to_delete = "// i[ @class ='oxd-icon bi-trash oxd-button-icon']"

    def input_username(self, username):
        self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_passward(self, password):
        self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()

    def click_pim_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.pim_button_locator).click()

    def click_delete_icon(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_delete_locator).click()

    def click_to_yes(self):
        self.loginpage_driver.find_element(By.XPATH, self.sure_to_delete).click()



