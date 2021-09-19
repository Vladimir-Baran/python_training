from model.contact import Contact

def test_del(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    app.contact.delete_first()