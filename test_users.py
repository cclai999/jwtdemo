from user_model import db_users

def test_valid_user():
    expected = True
    result = db_users.is_valid_user(id='test',pw='tung-test')
    assert result == expected

def test_invalid_user():
    expected = False
    result = db_users.is_valid_user(id='test',pw='test')
    assert result == expected