from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class projectohm:
    def __init__(self, driver):
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    login_button_locator = "//form/div[3]/button"
    invalid_crd_locator = "//p[text()='Invalid credentials']"
    login_locator = "// div[@class ='orangehrm-login-layout']"

    def input_username(self, username):
        self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_password(self, password):
        self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()

    # def wait_for_dashboard(driver):
    #     dashboard_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']")))
    #     return dashboard_element

    def verify_invalid_crd_locator(self):
        invalid_element = WebDriverWait(self.loginpage_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.verify_invalid_crd_locator)))
        return invalid_element.is_displayed()

