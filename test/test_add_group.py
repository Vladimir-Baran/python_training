# -*- coding: utf-8 -*-
from model.group import Group, Login


def test_add_group(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.create(Group(name="test", header="second", footer="first"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(Login(username="admin", password="secret"))
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

