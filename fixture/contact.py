from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")
                and len(wd.find_elements_by_name("searchstring")) > 0):
            # для уточнения я мог написать find_elements_by_link text("Send e-Mail")
            wd.find_element_by_link_text("home").click()

    def add_new(self, new_client):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_link_text("add new").click()
        self.change_data(new_client)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

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

    def edit_first_contact(self):
        self.modify_contact_by_index(0)
        self.contact_cache = None

    def modify_contact_by_index(self, index, client):
        wd = self.app.wd
        self.open_start_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//td[8]/a/img").click()
        self.change_data(client)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        self.select_contact_by_index(index)
        # wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count_contact(self):
        wd = self.app.wd
        self.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_start_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr")[1:]:
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=text1, firstname=text2, id=id))
        return list(self.contact_cache)

