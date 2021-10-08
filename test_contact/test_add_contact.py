from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) +1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



