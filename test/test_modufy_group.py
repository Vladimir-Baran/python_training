from model.login import Login
from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group1"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header1"))

def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New footer1"))