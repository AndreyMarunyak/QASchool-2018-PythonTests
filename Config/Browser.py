import pickle

from Config.Data import DRIVERPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chrome():

    #disable notifications
    chrome_options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values.notifications': 2}
    chrome_options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(executable_path=DRIVERPATH, chrome_options=chrome_options)

def saveCookies(browser):
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))

def loadCookies(browser):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

def wait(browser):
    return WebDriverWait(browser, 30)
