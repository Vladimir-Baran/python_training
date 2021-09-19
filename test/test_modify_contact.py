from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    app.contact.edit_first_contact(Contact(firstname="123", middlename="456", lastname="789", nickname="098",
                                           company="test", address="one", home_number="79993338822", bday="1",
                                           bmonth="April", byear="1976", mobile="79555555555", fax="75555555555"))

