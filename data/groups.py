# import random
# import string
from model.group import Group

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

testdata = constant
#
# def random_string(prefix, maxlen):
#     symbol = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), footer=random_string("footer", 10), header=random_string("header", 10))
#     for i in range(4)]