from model.group import Group
from random import randrange
from model.contact import Contact


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="random", home_number="87326352378", work="73652363281",
                                    mobile="328744653263", phone2="87439847362"))
    old_contact_in_db = db.count_contact_in_group()
    if len(app.contact.get_contact_list_in_none_group()) == 0:
        app.contact.add_new(Contact(firstname="random", home_number="87326352378", work="73652363281",
                                    mobile="328744653263", phone2="87439847362"))
        app.contact.open_none_group()
    old_contacts = app.contact.get_contact_list_in_none_group()
    index = randrange(len(old_contacts))
    contacts = old_contacts[index]
    app.contact.add_in_group(contacts.id)
    new_contact_in_db = db.count_contact_in_group()
    assert old_contact_in_db +1 == new_contact_in_db