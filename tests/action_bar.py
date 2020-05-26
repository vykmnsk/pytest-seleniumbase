import pytest
from navigation import openCategoryPage

bar = 'div[data-id="action-bar"]'
headerDesktop_home = f'{bar} h1[data-id="actionbar-heading-desktop"]'
headerMobile_home = f'{bar} h1[data-id="actionbar-heading-mobile"]'
headerDesktop_cat = f'{bar} h3[data-id="actionbar-heading-desktop"]'
headerMobile_cat = f'{bar} h3[data-id="actionbar-heading-mobile"]'
buttonBack = f'{bar} button'
HEADER = 'Help & Support'


@pytest.mark.desktop
def test_header_desktop(sb):
    sb.assert_text(HEADER, headerDesktop_home)
    sb.assert_element_not_visible(headerMobile_home)
    sb.assert_element_not_visible(buttonBack)


@pytest.mark.mobile
def test_mobile_header_no_back_btn_home(sb):
    sb.assert_text(HEADER, headerMobile_home)
    sb.assert_element_not_visible(headerDesktop_home)
    sb.assert_element_not_visible(buttonBack)


@pytest.mark.desktop
def test_header_non_home_desktop(sb):
    openCategoryPage(sb)
    sb.assert_element_not_visible(headerMobile_home)
    sb.assert_element_not_visible(buttonBack)


@pytest.mark.mobile
def test_mobile_header_back_btn_cat_page(sb):
    openCategoryPage(sb)
    sb.assert_text(HEADER, headerMobile_cat)
    sb.assert_element_not_visible(headerDesktop_cat)
    sb.assert_element_visible(buttonBack)


@pytest.mark.mobile
def test_tap_back_btn(sb, homeUrl):
    pytest.xfail("back btn doesn't work with proxy")
    openCategoryPage(sb)
    sb.assert_element_visible(buttonBack)
    sb.click(buttonBack)
    assert sb.get_current_url() == homeUrl


