from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, title=None, company=None, homephone=None, mobilephone=None,
                 workphone=None, email=None, email2=None, email3=None, address=None, bday=None, bmonth=None,
                 byear=None, all_phones_from_home_page=None, all_emails_from_home_page=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.firstname}:{self.lastname}:{self.email}"

    def __eq__(self, other):
        return (
                self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
