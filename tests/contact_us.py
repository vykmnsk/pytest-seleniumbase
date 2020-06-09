import pytest
from anytest import retry, TIMEOUT_MAX

contactUs = '[data-id="chat"]'
contactUsHeader = f'{contactUs} h3'
HEADER = 'Get more support'

chat = '[data-id="live-chat"]'
chatHeader = f'{chat} h4'
chatStatus = f'{chat} [data-id="status-label"]'
chatButton = f'{chat} button'
CHAT_HEADER = 'Chat with us'
CHAT_STATUS_AVAIL = 'Available'
CHAT_STATUS_UNAVAIL = 'Unavailable'
CHAT_STATUS_BUSY = 'Busy'
CHAT_STATUS_LOADING = 'Please wait'
CHAT_BUTTON_LABEL = "Let's chat"

messenger = '[data-id="chat-item-messenger"]'
messengerHeader = f'{messenger} h4'
messengerLink = f'{messenger} a'
MESSENGER_HEADER = 'Connect via Messenger'
MESSENGER_HREF_PART = 'http://m.me/'

phEmail = '[data-id="chat-item-other"]'
phEmailHeader = f'{phEmail} h4'
phEmailLink = f'{phEmail} a'
PH_EMAIL_HEADER = 'Phone or email'
PH_EMAIL_HREF_PART = '/contact.html'


def test_contactus_header(sb):
    sb.assert_element(contactUs)
    assert HEADER == sb.get_text(contactUsHeader)


def test_chat_header(sb):
    sb.assert_element(chat, timeout=TIMEOUT_MAX)
    sb.assert_text(CHAT_HEADER, chatHeader)


def test_chat_init_status(sb):
    sb.assert_element(chat, timeout=TIMEOUT_MAX)
    statusInit = sb.get_text(chatStatus)
    assert statusInit == CHAT_STATUS_LOADING


def test_chat_status_n_button(sb):
    sb.assert_element(chat, timeout=TIMEOUT_MAX)
    status = None

    def assert_loadedStatus():
        status = sb.get_text(chatStatus)
        assert status in [
            CHAT_STATUS_AVAIL,
            CHAT_STATUS_UNAVAIL,
            CHAT_STATUS_BUSY]
    retry(assert_loadedStatus, 5, 2)

    if status == CHAT_STATUS_AVAIL:
        sb.assert_element(chatButton)
        sb.assert_text(CHAT_BUTTON_LABEL, chatButton)


def test_messenger_header_n_link(sb):
    sb.assert_element(messenger, timeout=TIMEOUT_MAX)
    sb.assert_text(MESSENGER_HEADER, messengerHeader)
    assert MESSENGER_HREF_PART in sb.get_attribute(messengerLink, 'href')


def test_phone_email_header(sb):
    sb.assert_text(PH_EMAIL_HEADER, phEmailHeader)
    assert PH_EMAIL_HREF_PART in sb.get_attribute(phEmailLink, 'href')
