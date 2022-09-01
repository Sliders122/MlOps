def check_user_name(user_name):
    """ Not empty string. No spaces. """
    if user_name == "":
        return False
    if " " in user_name:
        return False
    else:
        return True


def test_empty_user_name():
    """ Test if check_user_name() returns False for empty string. """
    assert check_user_name("") == False


def test_space_user_name():
    """ Test if check_user_name() returns False for string with spaces. """
    assert check_user_name("Qu entin") == False
    assert check_user_name("Quentin ") == False
    assert check_user_name(" Quentin") == False


def test_valid_user_name():
    """ test if check_user_name() returns True for valid string. """
    assert check_user_name("Quentin") == True
