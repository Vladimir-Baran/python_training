from fixture.application import Application
import pytest
from model.login import Login
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(Login(username=web_config["username"], password=web_config["password"]))
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        fixture.session.ensure_logout()
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_gr"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("data_co"):
            testdatacontact = load_form_module_contact(fixture[5:])
            metafunc.parametrize(fixture, testdatacontact, ids=[str(x) for x in testdatacontact])
        elif fixture.startswith("json_groups"):
            testdata = load_form_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_contact"):
            testdatacontact = load_form_json_contact(fixture[5:])
            metafunc.parametrize(fixture, testdatacontact, ids=[str(x) for x in testdatacontact])

def load_form_module_contact(module):
    return importlib.import_module("data.%s" % module).testdatacontact

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_form_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/groups.json")) as q:
        return jsonpickle.decode(q.read())

def load_form_json_contact(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/contacts.json")) as f:
        return jsonpickle.decode(f.read())

