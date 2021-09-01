# -*- coding: utf-8 -*-
from group import Login
from client import New_client
import pytest
from application import Application
from client import New_client
from group import Login


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_client(app):
    app.login(Login(username="admin", password="secret"))
    app.add_new_client(New_client(firstname="Vladimir", middlename="Baran", lastname="Test", nickname="QA",
                                       company="Bell", address="Street", home_number="79999999999", bday="1",
                                       bmonth="April", byear="1991", group="test"))
    app.logout()

