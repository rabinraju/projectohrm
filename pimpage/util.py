from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_pim(driver):
    pim_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
    return pim_element


