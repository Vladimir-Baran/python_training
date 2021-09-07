from selenium.webdriver.support.ui import Select


class Contact:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_new(self, client):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_link_text("add new").click()
        self.change_data(client)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_start_page()

    def change_data(self, client):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(client.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(client.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(client.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(client.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(client.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(client.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(client.home_number)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(client.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(client.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(client.byear)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(client.mobile)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(client.fax)

    def edit_first_contact(self, client):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//td[8]/a/img").click()
        self.change_data(client)
        wd.find_element_by_name("update").click()
        self.open_start_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_start_page()


