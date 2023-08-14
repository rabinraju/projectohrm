import json
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from orangehrmpages.utilites.utils import wait_for_login
import time
from orangehrmpages.utilites.utils import wait_for_dashboard
from projectohm.tc_Login_01 import projectohm


class loginohrm(unittest.TestCase):
    driver = None

    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Test case ID: TC_Login_01")
        print("Test case ID: TC_Login_02")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        json_file_path = "C:\\Users\\antho\\PycharmProjects\\pythonProject3\\datasource\\test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    def tearDownClass(cls) -> None:
        print("The user is logged in successfully.")
        print("A valid error message for invalid credentials is displayed")

    def test_successfully_login(self):
        hrmloginobject = projectohm(self.driver)
        hrmloginobject.input_username(self.data_dict.get("Login_test_data").get("correct_username"))
        hrmloginobject.input_password(self.data_dict.get("Login_test_data").get("correct_password"))
        hrmloginobject.click_login()
        time.sleep(12)
        assert wait_for_dashboard(self.driver)
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.find_element(By.XPATH, "//img[@class='oxd-userdropdown-img']").click()
        time.sleep(4)
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")))
        time.sleep(5)
        logout_button.click()
        time.sleep(7)

    def test_wrong_password(self):
        hrmloginobject = projectohm(self.driver)
        hrmloginobject.input_username(self.data_dict.get("Login_test_data").get("correct_username"))
        hrmloginobject.input_password(self.data_dict.get("Login_test_data").get("incorrect_password"))
        time.sleep(2)
        hrmloginobject.click_login()
        time.sleep(4)







