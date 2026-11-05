from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="firstname_mod"))


def test_modify_contact_birthdate(app):
    app.contact.modify_first_contact(Contact(bday="21", bmonth="November", byear="1985"))
