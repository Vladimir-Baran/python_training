from model.contact import Contact


def test_add_new_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(
        firstname="1", middlename="Baran", lastname="Test", nickname="QA",
        company="Bell", address="Street", home_number="79999999999", bday="1",
        bmonth="April", byear="1991", mobile="71111111111", fax="72222222222"
    )
    app.contact.add_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) +1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



