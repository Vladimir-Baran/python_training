import re
from model.contact import Contact

def test_all_info_on_home_page(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", home_number="87326352378", work="73652363281",
                                    mobile="328744653263", phone2="87439847362"))
    list = list()
    contact_from_home_page = app.contact.get_contact_list()[]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phone_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_phones_on_contact_view_page(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", home_number="87326352378", work="73652363281",
                                    mobile="328744653263", phone2="87439847362"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_number == contact_from_edit_page.home_number
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear(s):
    return re.sub("[ () -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.mobile, contact.work, contact.phone2]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))


