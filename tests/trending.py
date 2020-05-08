import pytest
from anytest import TIMEOUT_MAX

trending = 'div[data-id="trending"]'
header = f'{trending} h3'
questions = f'{trending} h4'
HEADER_UNAUTH = 'Trending questions'
HEADER_AUTH = 'You may also like'


def test_header_unauth(sb, homeUrl):
    sb.open(homeUrl)
    assert HEADER_UNAUTH == sb.get_text(header, timeout=TIMEOUT_MAX)


def test_header_auth(sb, homeUrlAuth):
    sb.open(homeUrlAuth)
    assert HEADER_AUTH == sb.get_text(header, timeout=TIMEOUT_MAX)


def test_questions_count_category_page(sb, catUrl):
    sb.open(catUrl)
    assert sb.get_current_url().endswith(catUrl)
    assertQuestionsCount(sb, 3)


@pytest.mark.desktop
def test_questions_count_home_desktop(sb, homeUrl):
    sb.open(homeUrl)
    assertQuestionsCount(sb, 6)


@pytest.mark.mobile
def test_questions_count_home_mobile(sb, homeUrl):
    sb.open(homeUrl)
    assertQuestionsCount(sb, 3)


def assertQuestionsCount(sb, count):
    sb.assert_element(trending, timeout=TIMEOUT_MAX)
    assert len(sb.find_visible_elements(questions)) == count
