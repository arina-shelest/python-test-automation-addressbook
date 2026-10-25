from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_one(
        Contact("firstname_mod", "lastname_mod", "title_mod", "company_mod", "test_mod@mail.com", "21", "November",
                "1985"))
    app.session.logout()
