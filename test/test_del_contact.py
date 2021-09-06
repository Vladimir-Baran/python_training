from model.login import Login


def test_del(app):
    app.session.login(Login(username="admin", password="secret"))
    app.client.delete_first()
    app.session.logout()