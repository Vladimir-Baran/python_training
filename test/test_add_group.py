# -*- coding: utf-8 -*-
from model.group import Group
from model.login import Login


def test_add_group(app):
    app.group.create(Group(name="test", header="second", footer="first"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

