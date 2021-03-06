from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, home_number=None,
                 bday=None, bmonth=None, byear=None, mobile=None, fax=None, id=None, work=None, all_phone_from_home_page = None,
                 all_email_from_home_page=None, email=None, email2=None, email3=None, phone2=None, new_group=None):
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
        self.work = work
        self.all_phone_from_home_page = all_phone_from_home_page
        self.email = email
        self.all_email_from_home_page = all_email_from_home_page
        self.email2 = email2
        self.email3 = email3
        self.phone2 = phone2
        self.new_group = new_group

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
             self.firstname, self.middlename, self.company,
            self.fax, self.mobile,
             self.byear, self.bmonth, self.bday,
             self.home_number, self.work, self.id,
            self.address, self.nickname, self.lastname,
             self.email, self.email2, self.email3, self.phone2, self.all_phone_from_home_page, self.all_email_from_home_page
        )

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
               and (self.fax is None or other.fax is None or self.fax == other.fax)   \
               and (self.work is None or other.work is None or self.work == other.work)   \
               and (self.email is None or other.email is None or self.email == other.email)   \
               and (self.email2 is None or other.email2 is None or self.email2 == other.email2)   \
               and (self.email3 is None or other.email3 is None or self.email3 == other.email3)   \
               and (self.phone2 is None or other.phone2 is None or self.phone2 == other.phone2)   \
               and (self.all_phone_from_home_page is None or other.all_phone_from_home_page is None
                    or self.all_phone_from_home_page == other.all_phone_from_home_page)   \
               and (self.all_email_from_home_page is None or other.all_email_from_home_page is None
                    or self.all_email_from_home_page == other.all_email_from_home_page)
