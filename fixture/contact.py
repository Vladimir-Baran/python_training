from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import random
from model.group import Group

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
        self.open_start_page()
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
        self.change_contact_field_value("byear", client.byear)
        self.change_contact_field_value("mobile", client.mobile)
        self.change_contact_field_value("fax", client.fax)
        self.change_contact_field_value("work", client.work)
        self.change_contact_field_value("phone2", client.phone2)

    def edit_first_contact(self):
        self.modify_contact_by_index(0)
        self.contact_cache = None

    def modify_contact_by_index(self, index, client):
        wd = self.app.wd
        self.open_start_page()
        self.open_contact_to_edit_by_index(index)
        self.change_data(client)
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, client):
        wd = self.app.wd
        self.open_start_page()
        self.open_for_modify_by_id(id)
        self.change_data(client)
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()
        self.contact_cache = None

    def add_in_group(self, id):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_link_text("groups").click()
        group = random.choice(self.get_group_value())
        self.open_none_group()
        self.select_checkbox_by_id(id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group)
        wd.find_element_by_name("add").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()

    def del_in_group_by_id(self, id):
        wd = self.app.wd
        group = random.choice(self.get_group_value())
        self.open_start_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group)
        self.select_checkbox_by_id(id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()

    def get_group_value(self):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_link_text("groups").click()
        group_cache = []
        for element in wd.find_elements_by_css_selector("span.group"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            group_cache.append(id)
        return list(group_cache)

    def open_none_group(self):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")

    def open_test_group(self):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text("test")

    def select_checkbox_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_for_modify_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("[href='edit.php?id=%s']" % id).click()

    def delete_first(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_start_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_start_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def number_of_contacts(self):
        wd = self.app.wd
        self.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    def number_fo_contacts_in_group(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def number_of_contacts_by_id(self, id):
        wd = self.app.wd
        self.open_start_page()
        wd.find_element_by_css_selector("input[value='%s']" % id)

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        self.open_start_page()
        entry = wd.find_elements_by_name("entry")
        if self.contact_cache is None:
            self.open_start_page()
            self.contact_cache = []
            for element in entry:
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id
                                                  , all_phone_from_home_page=all_phones
                                                  , address=address
                                                  , all_email_from_home_page = all_mails
                                                  ))
        return list(self.contact_cache)

    def get_contact_list_in_none_group(self):
        wd = self.app.wd
        self.open_start_page()
        self.open_none_group()
        entry = wd.find_elements_by_name("entry")
        if self.contact_cache is None:
            self.contact_cache = []
            for element in entry:
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id
                                                  , all_phone_from_home_page=all_phones
                                                  , address=address
                                                  , all_email_from_home_page = all_mails
                                                  ))
        return list(self.contact_cache)

    def get_contact_list_in_group(self):
        wd = self.app.wd
        group = random.choice(self.get_group_value())
        self.open_start_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group)
        entry = wd.find_elements_by_name("entry")
        if self.contact_cache is None:
            self.contact_cache = []
            for element in entry:
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id
                                                  , all_phone_from_home_page=all_phones
                                                  , address=address
                                                  , all_email_from_home_page = all_mails
                                                  ))
        return list(self.contact_cache)

    def random_contact_index(self):
        return random.randrange(self.number_of_contacts())

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_start_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_start_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_number=homephone, work=workphone, mobile=mobilephone, phone2=secondphone,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(home_number=homephone, work=workphone, mobile=mobilephone)
