from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import Contact

class Application:

    def __init__(self):
        # self.wd = webdriver.Chrome()
        self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.client = Contact(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()