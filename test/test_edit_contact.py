# -*- coding: utf-8 -*-

from model.contact import Edit_contact
from model.group import Login


def test_edit_contact(app):
    app.session.login(Login(username="admin", password="secret"))
    app.client.edit_first_contact(Edit_contact(address="stop", company="New",
                                               mobile="79111111111", fax="78766325533", home_number="79999999999"))
    app.session.logout()

