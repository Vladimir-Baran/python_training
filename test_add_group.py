# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from group import Login
import unittest

class test_add_group(unittest.TestCase):
    def setUp(self):
        # self.wd = webdriver.Chrome()
        self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        wd = self.wd
        self.login(wd, Login(username="admin", password="secret"))
        self.create_group(wd, Group(name="test", header="second", footer="first"))
        self.logout(wd)


    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, Login(username="admin", password="secret"))
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        self.open_group_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, login):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(login.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
