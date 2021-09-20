from fixture.application import Application
import pytest
from model.login import Login
from fixture import session

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        # fixture.session.ensure_login(Login(username="admin", password="secret"))
    else:
        if not fixture.is_valid():
            fixture = Application()
            # fixture.session.ensure_login(Login(username="admin", password="secret"))
    fixture.session.ensure_login(Login(username="admin", password="secret"))
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture