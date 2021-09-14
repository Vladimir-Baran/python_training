from model.login import Login
from model.group import Group

def test_modify_group_name(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.modify_first_group(Group(name="New group1"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.modify_first_group(Group(header="New header1"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.modify_first_group(Group(footer="New footer1"))
    app.session.logout()