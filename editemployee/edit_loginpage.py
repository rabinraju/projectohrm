from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class editemployee:

    def __init__(self, driver):
        # self.employeename = driver
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    login_button_locator = "//form/div[3]/button"
    pim_button_locator = "//span[text()='PIM']"
    click_editbutton_locator = "//button[@type='button'][2]"
    # clear_text = 'firstName'
    firstname_locator = "//input[@name='firstName']"
    middlename_locator = "//input[@name='middleName']"
    lastname_locator = "//input[@name='lastName']"
    job_button_locator = "//a[@class='orangehrm-tabs-item' and @href='/web/index.php/pim/viewJobDetails/empNumber/10' " \
                         "and @data-v-8cad1ea8='']"
    click_save_button = "//button[@type='submit']"

    def input_username(self, username):
        self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_passward(self, password):
        self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()

    def click_pim_button(self, ):
        self.loginpage_driver.find_element(By.XPATH, self.pim_button_locator).click()

    def click_editicon_button(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_editbutton_locator).click()

    # def clear_textbox(self, ):
    #     self.loginpage_driver.find_element(By.XPATH, self.clear_text).clear()

    def input_firstname(self, firstname):
        self.loginpage_driver.find_element(By.XPATH, self.firstname_locator).send_keys(firstname)

    def input_middlename(self, middlename):
        self.loginpage_driver.find_element(By.XPATH, self.middlename_locator).send_keys(middlename)

    def input_lastname(self, lastname):
        self.loginpage_driver.find_element(By.XPATH, self.lastname_locator).send_keys(lastname)
    #
    # def click_jobicon(self):
    #     self.loginpage_driver.find_element(By.XPATH, self.job_button_locator).click()
    #
    # def input_employee_status(self,Freelance):
    #     self.loginpage_driver.find_element(By.XPATH, self.Employment_Status_locator).send_key(Freelance)

    def click_savebutton(self):
        self.loginpage_driver.find_element(By.XPATH, self.click_save_button).click()

