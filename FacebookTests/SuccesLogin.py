from Config.Data import *
from Config.Browser import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time

POST_TEXT = 'Принёс жертву богу опп'

chrome = chrome()
chrome.implicitly_wait(30)

LOGIN = Data.LOGIN
PASSWORD = Data.PASSWORD
DRIVERPATH = Data.DRIVERPATH



class SuccessLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome.get(URL)

    def testLogin(self):

        chrome.find_element_by_id(EMAIL_FIELD).send_keys(LOGIN)
        chrome.find_element_by_id(PASS_FIELD).send_keys(PASSWORD)
        chrome.find_element_by_id(LOGIN_BUTTON).click()

        # save cookies for next test
        saveCookies(chrome)

        assert chrome.title == 'Facebook', 'Wrong title'

    def testPostAdding(self):

        chrome.find_element(By.XPATH, SEARCH_FIELD).send_keys('QA School 2018 - Kherson')
        chrome.send_keys(Keys.ENTER)
        chrome.find_element(By.XPATH, QA_SCHOOL_LINK).click()
        chrome.find_element(By.XPATH, POST_FIELD).send_keys(POST_TEXT)
        chrome.find_element(By.XPATH, SEND_POST_BUTTON).click()
        time.sleep(10)
        chrome.find_element(By.XPATH, COMMUNITY_BUTTON).click()
        time.sleep(5)
        chrome.find_element(By.XPATH, LIKE_BUTTON).click()
        assert (POST_TEXT in chrome.page_source)

    @classmethod
    def tearDownClass(cls):
        chrome.close()
        chrome.quit()


class SuccessPostAdding(unittest.TestCase):

    def setUp(self):

        if chrome.title != 'Facebook':
            chrome.get(URL)
            try:
                loadCookies(chrome)
                chrome.refresh()
            except Exception as e:
                print(e, ': no cookies file')




if __name__ == '__main__':
    unittest.main()

