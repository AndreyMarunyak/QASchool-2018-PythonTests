import LoginData

from selenium import webdriver

LOGIN = LoginData.LOGIN
PASSWORD = LoginData.PASSWORD

browser = webdriver.Chrome()


def login():
    browser.get('http://facebook.com')


class SomeTest():
    def first(self):
        pass

    def second(self):
        pass


if __name__ == '__main__':
    login()

