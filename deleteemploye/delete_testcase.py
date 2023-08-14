import json
import unittest
from selenium import webdriver
import time
from deleteemploye.delete_loginpage import delete


class deleteTestCase(unittest.TestCase):
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
        print("The user should be able to delete an existing employee information in the PIM and should see a message "
              "for successful deletion.")

    def test_succesfully(self):
        print("done")
        deletemodule = delete(self.driver)
        deletemodule.input_username((self.data_dict.get("Login_test_data").get("correct_username")))
        deletemodule.input_passward((self.data_dict.get("Login_test_data").get("correct_password")))
        deletemodule.click_login_button()
        time.sleep(1)
        deletemodule.click_pim_button()
        time.sleep(2)
        deletemodule.click_delete_icon()
        time.sleep(4)

    def test_yestodelete(self):
        deletemodule = delete(self.driver)
        deletemodule.click_to_yes()
        time.sleep(4)
