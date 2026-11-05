from model.contact import Contact


def test_add_full_contact(app):
    app.contact.create(Contact("John", "Smith", "Engineer", "Meta", "test@mail.com", "11", "October", "1986"))


def test_add_contact_mandatory_fields(app):
    app.contact.create(Contact(firstname="Jack", lastname="Lu", email="test1@mail.com"))
