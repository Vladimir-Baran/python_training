# -*- coding: utf-8 -*-

from model.edit_client import Edit_client
from model.group import Login


def test_edit_client(app):
    app.session.login(Login(username="admin", password="secret"))
    app.client.edit_client(Edit_client(firstname="Vladimir", middlename="Baran", lastname="Test", nickname="QA",
                                  company="Bell", address="Street", home_number="79999999999", bday="1",
                                  bmonth="April", byear="1991"))
    app.session.logout()

