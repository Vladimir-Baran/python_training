from model.group import Group
from random import randrange
from model.contact import Contact


def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="first", home_number="87326352378", work="73652363281",
                                    mobile="328744653263", phone2="87439847362"))
    count_id_db = db.count_contact_in_group()
    count_in_web = len(db.get_contact_list())
    count_group_list = len(db.get_group_list())
    if count_id_db != count_in_web * count_group_list :
        old_contact_in_db = db.count_contact_in_group()
        old_contact = db.get_contact_list()
        index = randrange(len(old_contact))
        contacts = old_contact[index]
        app.contact.add_in_group(contacts.id)
        new_contact_in_db = db.count_contact_in_group()
        assert old_contact_in_db +1 == new_contact_in_db
    else: app.destroy()