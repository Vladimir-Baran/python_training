from model.contact import Contact


def test_add_new_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contact = db.get_contact_list()
    app.contact.add_new(contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) +1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)



