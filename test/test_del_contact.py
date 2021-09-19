from model.login import Login


def test_del(app):
    app.client.delete_first()