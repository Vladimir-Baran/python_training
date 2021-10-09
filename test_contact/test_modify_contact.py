from model.contact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contacts = old_contact[index]
    contact = Contact(firstname="123", middlename="456", lastname="789", nickname="098",
                                           company="test", address="one", home_number="79993338822", bday="1",
                                           bmonth="April", byear="1976", mobile="79555555555", fax="75555555555")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_id(contacts.id, contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)