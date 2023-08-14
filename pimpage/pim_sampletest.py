import subprocess

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import unittest
from selenium import webdriver
import json
from pimpage.pim_login import pimpage
from selenium.webdriver.support import expected_conditions as EC

from pimpage.util import wait_for_pim


class pimTestCase(unittest.TestCase):
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
        print("The user should be able to add a new employee in the PIM and should see a message for successful "
              "employee addition")

    def test_succesfully(self):
        print("done")
        hrmlobject = pimpage(self.driver)
        hrmlobject.input_username((self.data_dict.get("Login_test_data").get("correct_username")))
        hrmlobject.input_passward((self.data_dict.get("Login_test_data").get("correct_password")))
        hrmlobject.click_login_button()
        time.sleep(1)
        hrmlobject.click_pim_button()
        time.sleep(2)
        hrmlobject.click_add_button()
        time.sleep(3)

    def test_testemployee(self):
        info = pimpage(self.driver)
        info.input_firstname("Rabin")
        time.sleep(4)
        info.input_middlename("Raju")
        time.sleep(3)
        info.input_lastname("SE")
        time.sleep(3)
        info.click_plus()
        time.sleep(5)
        script_path = "C:\\Users\\antho\\OneDrive\\Documents\\orange3.exe"
        subprocess.run(script_path, shell=True)
        time.sleep(7)
        info.click_submit_button()
        time.sleep(2)

    def test_uemployee(self):
        addemp = pimpage(self.driver)
        addemp.click_add_employee()
        time.sleep(4)

    def test_wemployee(self):
        waddemp = pimpage(self.driver)
        waddemp.input_firstname1("rabin")
        time.sleep(2)
        waddemp.input_middlename1("raju")
        waddemp.click_submit_button1()
        time.sleep(3)

