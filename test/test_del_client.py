from model.edit_client import Edit_client
from model.group import Login


def test_del(app):
    app.session.login(Login(username="admin", password="secret"))
    app.client.delete_first()
    app.session.logout()