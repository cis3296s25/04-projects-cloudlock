from BackEnd.Microsoft_Auth import get_secret_key
from BackEnd.Microsoft_Auth import authenticate_acct
from BackEnd.Microsoft_Auth import create_one_time_password
from BackEnd.Microsoft_Auth import verify_user_code
from pyotp import TOTP

def test_get_new_secret_key():
    assert get_secret_key("stellar") != None, \
        "Should return some kind of secret_key"

def test_get_old_secret_key():
    assert get_secret_key("star") == "XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII", \
        "Should match with the secret_key in the json"

def test_authenticate_account_correct():
    assert (authenticate_acct("star", "XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII") ==
            "otpauth://totp/CloudLockTeam:star?secret=XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII&issuer=CloudLockTeam"),\
        "Should return the right link based on name_of_user and secret_key"

def test_authenticate_account_incorrect():
    assert (authenticate_acct("new_star", "WVHSJ6A5TN7O3O2FKVNLS3FDESCESBCD") !=
            "otpauth://totp/CloudLockTeam:star?secret=XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII&issuer=CloudLockTeam"), \
        "Different name_of_user and secret_key shouldn't match the different link"

def test_create_one_time_password_is_not_none():
    assert create_one_time_password("XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII") != None, \
        "Making a random password with a valid secret_key should return not None"

def test_verify_incorrect_user_code():
    match_code = create_one_time_password("XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII")

    assert verify_user_code("", match_code) == False, \
        "The wrong code should return False"

def test_verify_correct_user_code():
    match_code = create_one_time_password("XFQBVN4AI6XQXJZG5AIO3LGPJECYMTII")

    assert verify_user_code(match_code.now(), match_code) == True, \
        "The correct code should return True"