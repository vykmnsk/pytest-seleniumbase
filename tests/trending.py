import pytest
from anytest import emulateAuth
from navigation import openCategoryPage


trending = 'div[data-id="trending"]'
header = f'{trending} h3'
questions = f'{trending} h4'
HEADER_UNAUTH = 'Trending questions'
HEADER_AUTH = 'You may also like'


def assertQuestionsCount(sb, count):
    sb.assert_element(trending)
    assert len(sb.find_visible_elements(questions)) == count


def test_header_auth(sb):
    emulateAuth(sb)
    assert HEADER_AUTH == sb.get_text(header)


def test_header_unauth(sb):
    assert HEADER_UNAUTH == sb.get_text(header)


@pytest.mark.desktop
def test_questions_count_home_desktop(sb):
    assertQuestionsCount(sb, 6)


@pytest.mark.mobile
def test_questions_count_home_mobile(sb):
    assertQuestionsCount(sb, 3)


def test_header_category_page(sb):
    openCategoryPage(sb)
    sb.assert_element(header)


def test_questions_count_category_page(sb):
    openCategoryPage(sb)
    assertQuestionsCount(sb, 3)






