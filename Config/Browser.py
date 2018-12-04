<<<<<<< HEAD
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By

from Config import Data, FindElement



def chrome():

    #disable notifications
    chrome_options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values.notifications': 2}
    chrome_options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(executable_path=Data.DRIVERPATH, chrome_options=chrome_options)

def saveCookies(browser):
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))

def loadCookies(browser):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

=======
from selenium import webdriver
from Config import Data


class Browser():

    @staticmethod
    def chrome():
        return webdriver.Chrome(executable_path=Data.DRIVERPATH)
>>>>>>> f31d7f2... add config files and refactor
