from model.group import Group
from random import randrange


def test_del_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contact_in_db = db.count_contact_in_group()
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contacts = old_contact[index]
    app.contact.del_in_group(contacts.id)
    new_contact_in_db = db.count_contact_in_group()
    assert old_contact_in_db - 1 == new_contact_in_db