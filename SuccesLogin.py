import LoginData

import unittest
from selenium import webdriver



LOGIN = LoginData.LOGIN
PASSWORD = LoginData.PASSWORD


class SomeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=LoginData.DRIVERPATH)
        self.url = 'http://facebook.com'

    def testOpenBrowser(self):
        driver = self.driver
        driver.get("http://facebook.com")
        driver.find_element_by_id('email').send_keys(LOGIN)
        driver.find_element_by_id('pass').send_keys(PASSWORD)
        driver.find_element_by_id('loginbutton').click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

