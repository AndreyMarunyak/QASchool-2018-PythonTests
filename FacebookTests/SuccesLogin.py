
from Config.Data import *
from Config.Browser import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time

POST_TEXT = 'Принёс жертву богу опп'

chrome = chrome()
chrome.implicitly_wait(30)
from Config import Data
from Config import Browser

import unittest

URL = 'http://facebook.com'

LOGIN = Data.LOGIN
PASSWORD = Data.PASSWORD
DRIVERPATH = Data.DRIVERPATH

chrome = Browser.Browser.chrome()


class SuccessLoginTest(unittest.TestCase):

    def setUp(self):
        chrome.get(URL)

    def testLogin(self):

        chrome.find_element_by_id(EMAIL_FIELD).send_keys(LOGIN)
        chrome.find_element_by_id(PASS_FIELD).send_keys(PASSWORD)
        chrome.find_element_by_id(LOGIN_BUTTON).click()

        # save cookies for next test
        saveCookies(chrome)

        assert chrome.title == 'Facebook', 'Wrong title'

    def testOpenBrowser(self):

        chrome.find_element_by_id('email').send_keys(LOGIN)
        chrome.find_element_by_id('pass').send_keys(PASSWORD)
        chrome.find_element_by_id('loginbutton').click()
        print(chrome.title)
        assert chrome.title == 'Facebook'

    def tearDown(self):
        chrome.close()
        chrome.quit()


class SuccessPostAdding(unittest.TestCase):

    def setUp(self):
        loadCookies(chrome)
        chrome.get(URL)
        # chrome.refresh()

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


if __name__ == '__main__':
    unittest.main()

