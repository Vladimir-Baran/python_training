import random

from model.contact import Contact
import random

def test_del(app, check_ui, db):
    if db.get_contact_list() == 0:
        app.contact.add_new(Contact(firstname="first", bday="7", bmonth="April"))
    old_contact = db.get_contact_list()
    content = random.choice(old_contact)
    app.contact.delete_contact_by_id(content.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(content)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)