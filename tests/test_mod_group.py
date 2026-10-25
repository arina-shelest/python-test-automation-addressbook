from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_one(Group(name="group_mod", header="header_mod", footer="footer_mod"))
    app.session.logout()
