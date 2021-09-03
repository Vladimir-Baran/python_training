class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, company, address, home_number, bday, bmonth,
                       byear):
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

class Edit_contact:

    def __init__(self, company, mobile, fax, address, home_number):

        self.company = company
        self.address = address
        self.home_number = home_number
        self.mobile = mobile
        self.fax = fax