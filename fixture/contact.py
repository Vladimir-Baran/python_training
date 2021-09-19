from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new(self, new_client):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_link_text("add new").click()
        self.change_data(new_client)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_data(self, client):
        wd = self.app.wd
        self.change_contact_field_value("firstname", client.firstname)
        self.change_contact_field_value("middlename", client.middlename)
        self.change_contact_field_value("lastname", client.lastname)
        self.change_contact_field_value("nickname", client.nickname)
        self.change_contact_field_value("company", client.company)
        self.change_contact_field_value("address", client.address)
        self.change_contact_field_value("home", client.home_number)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(client.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(client.bmonth)
        self.change_contact_field_value("byear", client.byear)
        self.change_contact_field_value("mobile", client.mobile)
        self.change_contact_field_value("fax", client.fax)

    def edit_first_contact(self, client):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//td[8]/a/img").click()
        self.change_data(client)
        wd.find_element_by_name("update").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def count_contact(self):
        wd = self.app.wd
        self.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

