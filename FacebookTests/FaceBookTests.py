import time

from Config.Data import *
from Config.Browser import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import unittest

POST_TEXT = 'Носолин'

chrome = chrome()
chrome.implicitly_wait(30)

class FacebookTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome.get(URL)

    def test_1_Login(self):

        chrome.find_element_by_id(EMAIL_FIELD).send_keys(LOGIN)
        chrome.find_element_by_id(PASS_FIELD).send_keys(PASSWORD)
        chrome.find_element_by_id(LOGIN_BUTTON).click()

        # save cookies for next test
        saveCookies(chrome)

        assert chrome.title == 'Facebook', 'Wrong title'

    def test_2_PostAdding(self):

        isLoginCheck(chrome)

        chrome.find_element(By.XPATH, SEARCH_FIELD).send_keys('QA School 2018 - Kherson')
        chrome.find_element(By.XPATH, SEARCH_FIELD).send_keys(Keys.ENTER)
        chrome.find_element(By.XPATH, QA_SCHOOL_LINK).click()
        chrome.find_element(By.XPATH, POST_FIELD).send_keys(POST_TEXT)
        chrome.find_element(By.XPATH, SEND_POST_BUTTON).click()

        wait(chrome).until(EC.presence_of_element_located((By.XPATH, SUCCESS_POST_ADDING_MESSAGE)))

        chrome.find_element(By.XPATH, COMMUNITY_BUTTON).click()

        wait(chrome).until(EC.presence_of_element_located((By.XPATH, FIRST_POST_ON_WALL)))

        assert (POST_TEXT in chrome.page_source)

    def test_3_LikeAdding(self):

        isLoginCheck(chrome)

        chrome.find_element(By.XPATH, SEARCH_FIELD).send_keys('QA School 2018 - Kherson')
        chrome.find_element(By.XPATH, SEARCH_FIELD).send_keys(Keys.ENTER)
        chrome.find_element(By.XPATH, QA_SCHOOL_LINK).click()
        chrome.find_element(By.XPATH, COMMUNITY_BUTTON).click()

        like_button = chrome.find_element(By.XPATH, LIKE_BUTTON)

        self.assertTrue(likeButtonIsClicked(like_button), 'Like have not been added')

    def test_4_Logout(self):

        isLoginCheck(chrome)

        chrome.find_element(By.ID, LOGOUT_MENU).click()
        chrome.find_element(By.XPATH, LOGOUT_BUTTON).click()
        self.assertTrue(isLogoutCheck(chrome))

    @classmethod
    def tearDownClass(cls):
        chrome.close()
        chrome.quit()


if __name__ == '__main__':
    unittest.main()

