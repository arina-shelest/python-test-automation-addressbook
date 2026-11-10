from random import randrange
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact_firstname", lastname="contact_lastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname_mod")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_birthdate(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="contact_firstname", lastname="contact_lastname"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(bday="21", bmonth="November", byear="1985"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
