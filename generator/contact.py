import os.path
import jsonpickle
import getopt
import sys
import random
import string
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o, a in opts:
        if o == "-n":
            n=int(a)
        elif o == "-f":
            f = a

def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbol = string.digits
    return "7".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdatacontact = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="",
            home_number="78888888888", mobile="88888888888", fax="99999999999", work="78475746583", phone2="7283472873723")] + [Contact(
    firstname=random_string("firs", 10), middlename=random_string("header", 10), lastname=random_string("lastname", 10),
    nickname=random_string("nick", 10), company=random_string("company", 10), address=random_string("address", 10),
    home_number=random_number(11), mobile=random_number(11), fax=random_number(11)) for i in range(5)]
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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdatacontact))