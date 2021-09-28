from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, home_number=None,
                 bday=None, bmonth=None, byear=None, mobile=None, fax=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_number = home_number
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.mobile = mobile
        self.fax = fax
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s%s" % (self.id, self.firstname, self.middlename)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.middlename == other.middlename
