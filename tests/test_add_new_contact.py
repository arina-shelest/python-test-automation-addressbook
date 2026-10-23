import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_full_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact("John", "Smith", "Engineer", "Meta", "test@mail.com", "11", "October", "1986"))
    app.logout()


def test_add_contact_mandatory_fields(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Jack", lastname="Lu", email="test1@mail.com"))
    app.logout()
