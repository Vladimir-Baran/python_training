from model.contact import Contact
from random import randrange

def test_del(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact [index:index+1] = []
    assert old_contact == new_contact