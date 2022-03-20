import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


class FormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_valid_form(self):
        """
        Automated test for submitting valid form
        """
        driver = self.driver
        driver.get("https://ultimateqa.com/filling-out-forms/")

        self.assertIn("Filling Out Forms | Ultimate QA", driver.title)
        driver.find_element_by_id("et_pb_contact_name_0").click()
        driver.find_element_by_id("et_pb_contact_name_0").send_keys("Bash Test")
        driver.find_element_by_id("et_pb_contact_message_0").click()
        driver.find_element_by_id("et_pb_contact_message_0").send_keys("This is a message")
        WebDriverWait(driver, 15)
        driver.find_element_by_css_selector("#et_pb_contact_form_0 > div.et_pb_contact > form > div > button").click()

    def tearDown(self):
        self.driver.quit()
