from model.login import Login


def test_delete_first_group(app):
    app.group.delete_first()
