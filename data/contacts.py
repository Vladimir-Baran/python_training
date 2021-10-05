import random
import string
from model.contact import Contact



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