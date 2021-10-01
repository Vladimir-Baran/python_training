from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbol = string.digits
    return "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdatacontact = [
    Contact(
        firstname=firstname, middlename=middlename, lastname=lastname, nickname=nick, company=company, address=address,
            home_number=home_number, mobile=mobile,
        fax=fax)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("header", 20)]
    for lastname in ["", random_string("lastname", 20)]
    for nick in ["", random_string("nick", 20)]
    for company in ["", random_string("company", 20)]
    for address in ["", random_string("address", 20)]
    for home_number in ["", random_number(11)]
    for mobile in ["", random_number(11)]
    for fax in ["", random_number(11)]
]

@pytest.mark.parametrize("contact", testdatacontact, ids=[repr(x) for x in testdatacontact])
def test_add_new_contact(app, contact):
    # pass
    old_contact = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) +1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



