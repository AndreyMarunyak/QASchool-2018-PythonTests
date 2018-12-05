import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.Data import DRIVERPATH, EMAIL_FIELD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Config.Data import URL

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

def isLoginCheck(browser):
    if isLogoutCheck(browser):
        browser.get(URL)
        try:
            loadCookies(browser)
            browser.refresh()
        except Exception as e:
            print(e, ': no cookies file')

def likeButtonIsClicked(button):

    # maybe Regex would be better

    source_defore_click = button.get_attribute('innerHTML')

    button.click()
    time.sleep(3) # i don't know how to do it better

    source_after_click = button.get_attribute('innerHTML')

    return source_defore_click != source_after_click

def isLogoutCheck(browser):
    try:
        browser.find_element(By.ID, EMAIL_FIELD)
    except NoSuchElementException:
        return False
    return True