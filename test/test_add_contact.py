# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact
from model.login import Login


def test_add_new_contact(app):
    app.client.add_new(Contact(firstname="1", middlename="Baran", lastname="Test", nickname="QA",
                               company="Bell", address="Street", home_number="79999999999", bday="1",
                               bmonth="April", byear="1991", mobile="71111111111", fax="72222222222"))

