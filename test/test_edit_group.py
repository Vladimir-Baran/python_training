from model.group import Group
from model.login import Login

def test_add_group(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.create(Group(name="test", header="second", footer="first"))
    app.session.logout()