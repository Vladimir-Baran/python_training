from model.group import Group
from model.login import Login

def test_add_group(app):
    app.group.create(Group(name="test", header="second", footer="first"))