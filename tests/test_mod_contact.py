from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact_firstname", lastname="contact_lastname"))
    app.contact.modify_first_contact(Contact(firstname="firstname_mod"))


def test_modify_contact_birthdate(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact_firstname", lastname="contact_lastname"))
    app.contact.modify_first_contact(Contact(bday="21", bmonth="November", byear="1985"))
