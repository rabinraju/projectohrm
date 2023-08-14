from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import unittest
from selenium import webdriver
import json
from editemployee.edit_loginpage import editemployee


class editTestCase(unittest.TestCase):
    driver = None

    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(4)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        json_file_path = "C:\\Users\\antho\\PycharmProjects\\pythonProject3\\datasource\\test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    @classmethod
    def tearDownClass(cls) -> None:
        print("The user should be able to edit an existing employee information in the PIM and should see a message "
              "for successful employee details additions")

    def test_succesfully(self):
        print("done")
        editmodule = editemployee(self.driver)
        editmodule.input_username((self.data_dict.get("Login_test_data").get("correct_username")))
        editmodule.input_passward((self.data_dict.get("Login_test_data").get("correct_password")))
        editmodule.click_login_button()
        time.sleep(1)
        editmodule.click_pim_button()
        time.sleep(2)
        editmodule.click_editicon_button()
        time.sleep(4)

    def test_testadddata(self):
        info = editemployee(self.driver)
        info.input_firstname("Rabin")
        time.sleep(4)
        info.input_middlename("Raju")
        time.sleep(3)
        info.input_lastname("SE")
        time.sleep(4)
        # info.click_jobicon()
        # time.sleep(4)
        info.click_savebutton()
        time.sleep(6)



