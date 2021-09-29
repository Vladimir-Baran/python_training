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
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.middlename, self.company, self.fax,
                            self.mobile, self.byear, self.bmonth, self.bday, self.home_number,
                            self.address, self.nickname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.middlename is None or other.middlename is None or self.middlename == other.middlename) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)  \
               and (self.nickname is None or other.nickname is None or self.nickname == other.nickname)  \
               and (self.company is None or other.company is None or self.company == other.company)  \
               and (self.address is None or other.address is None or self.address == other.address)  \
               and (self.home_number is None or other.home_number is None or self.home_number == other.home_number)  \
               and (self.bday is None or other.bday is None or self.bday == other.bday)  \
               and (self.bmonth is None or other.bmonth is None or self.bmonth == other.bmonth)  \
               and (self.byear is None or other.byear is None or self.byear == other.byear)  \
               and (self.mobile is None or other.mobile is None or self.mobile == other.mobile)   \
               and (self.fax is None or other.fax is None or self.fax == other.fax)
