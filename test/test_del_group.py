from model.group import Login, Group


def test_delete_first_group(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.delete_first()
    app.session.logout()
