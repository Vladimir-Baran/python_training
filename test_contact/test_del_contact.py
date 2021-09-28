from model.contact import Contact

def test_del(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    app.contact.delete_first()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact [0:1] = []
    assert old_contact == new_contact