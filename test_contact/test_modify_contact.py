from model.contact import Contact


def test_edit_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    contact = Contact(firstname="123", middlename="456", lastname="789", nickname="098",
                                           company="test", address="one", home_number="79993338822", bday="1",
                                           bmonth="April", byear="1976", mobile="79555555555", fax="75555555555")
    contact.id = old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)