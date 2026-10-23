import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_full_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("John", "Smith", "Engineer", "Meta", "test@mail.com", "11", "October", "1986"))
    app.session.logout()


def test_add_contact_mandatory_fields(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Jack", lastname="Lu", email="test1@mail.com"))
    app.session.logout()
