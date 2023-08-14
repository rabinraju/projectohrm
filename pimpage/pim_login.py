import app as app
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class pimpage:

    def __init__(self, driver):
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    login_button_locator = "//form/div[3]/button"
    pim_button_locator = "//span[text()='PIM']"
    add_button_locator = "//button[text()=' Add ']"
    clear_text = "//input[@name='firstName']"
    firstname_locator = "//input[@name='firstName']"
    middlename_locator = "//input[@name='middleName']"
    lastname_locator = "//input[@name='lastName']"
    click_plus_locator = "//i[@class='oxd-icon bi-plus']"
    script_path = "C:\\Users\\antho\\OneDrive\\Documents\\orange2.exe"
    submit_button_locator = "//button[@type='submit']"
    add_employee_locator = "//a[text()='Add Employee']"
    firstname1_locator = "//input[@name='firstName']"
    middlename2_locator = "//input[@name='middleName']"
    submit_button1_locator = "//button[@type='submit']"

    # login
    def input_username(self, username):
        self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_passward(self, password):
        self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()

    def click_pim_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.pim_button_locator).click()

    def click_add_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.add_button_locator).click()

    def clear_textbox(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.clear_text).clear()

    # try
    def input_firstname(self, firstname):
        self.loginpage_driver.find_element(By.XPATH, self.firstname_locator).send_keys(firstname)

    def input_middlename(self, middlename):
        self.loginpage_driver.find_element(By.XPATH, self.middlename_locator).send_keys(middlename)

    def input_lastname(self, lastname):
        self.loginpage_driver.find_element(By.XPATH, self.lastname_locator).send_keys(lastname)

    def click_plus(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_plus_locator).click()

    def click_submit_button(self):
        self.loginpage_driver.find_element(By.XPATH, self.submit_button_locator).click()

    def click_add_employee(self):
        self.loginpage_driver.find_element(By.XPATH, self.add_employee_locator).click()

    def input_firstname1(self, firstname):
        self.loginpage_driver.find_element(By.XPATH, self.firstname1_locator).send_keys(firstname)

    def input_middlename1(self, middlename):
        self.loginpage_driver.find_element(By.XPATH, self.firstname1_locator).send_keys(middlename)

    def click_submit_button1(self):
        self.loginpage_driver.find_element(By.XPATH, self.submit_button1_locator).click()
