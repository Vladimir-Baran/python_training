from model.contact import Contact
import random
import string
import pytest
import time

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbol = string.digits
    return "7".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdatacontact = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="",
            home_number="", mobile="", fax="")] + [Contact(
    firstname=random_string("firs", 10), middlename=random_string("header", 10), lastname=random_string("lastname", 10),
    nickname=random_string("nick", 10), company=random_string("company", 10), address=random_string("address", 10),
    home_number=random_number(11), mobile=random_number(11), fax=random_number(11)) for i in range(3)]
    # for firstname in ["", random_string("firstname", 10)]
    # for middlename in ["", random_string("header", 20)]
    # for lastname in ["", random_string("lastname", 20)]
    # for nick in ["", random_string("nick", 20)]
    # for company in ["", random_string("company", 20)]
    # for address in ["", random_string("address", 20)]
    # for home_number in ["", random_number(11)]
    # for mobile in ["", random_number(11)]
    # for fax in ["", random_number(11)]
# ]

@pytest.mark.parametrize("contact", testdatacontact, ids=[repr(x) for x in testdatacontact])
def test_add_new_contact(app, contact):
    # pass
    old_contact = app.contact.get_contact_list()
    app.contact.add_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) +1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



