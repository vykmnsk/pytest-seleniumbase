import pytest
from anytest import retry, TIMEOUT_MED


username = "[data-id='login_usernameInput']"
password = "[data-id='PasswordInput']"
btnLogin = "[data-id='LoginStep__continue']"
loginUrl = '/login'

callAction = '[data-id="callToActionCard"]'
callActionButton = f'{callAction} button'

LABEL_LOG_IN = 'Log in'
LABEL_LOGGED_IN = 'Get in touch'
FORM_HEADER_LOGIN = 'Log in to My Account'
TEXT_LOG_IN = "Log in for help and support we've tailored for you."
TEXT_LOGGED_IN = "Couldn’t find your answer? Send us a message, we’ll come back to you."
HEADER_ACCOUNT = 'My Account'
LABEL_HELP = 'Help'

def enterLoginCreds(sb):
    usr, pwd = sb.data.split(':')

    def assert_loginURL():
        assert loginUrl in sb.get_current_url()

    def assert_notLoginURL():
        assert loginUrl not in sb.get_current_url()
       
    retry(assert_loginURL, 5, 1)
    sb.assert_text(FORM_HEADER_LOGIN, timeout=10)
    sb.update_text(username, usr)
    sb.update_text(password, pwd)
    sb.click(btnLogin)
    retry(assert_notLoginURL, 5, 1)


@pytest.mark.new
def test_login_box(sb):
    assert LABEL_LOG_IN == sb.get_text(callActionButton)
    assert TEXT_LOG_IN in sb.get_text(callAction)


@pytest.mark.last
@pytest.mark.login
def test_log_in(sb):
    sb.click_link_text(LABEL_LOG_IN, callActionButton)
    enterLoginCreds(sb)
    sb.wait_for_text(HEADER_ACCOUNT)
    sb.click_partial_link_text(LABEL_HELP)
    assert LABEL_LOGGED_IN == sb.get_text(callActionButton)
    assert TEXT_LOGGED_IN in sb.get_text(callAction)

