from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get('https://woocommerce-850415-2933260.cloudwaysapps.com/my-account')
        self.driver.find_element(By.ID, "username").send_keys("test_customer")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

if __name__ == "__main__":
    unittest.main()








