import pytest

bar = 'div[data-id="action-bar"]'
headerDesktop_home = f'{bar} h1[data-id="actionbar-heading-desktop"]'
headerMobile_home = f'{bar} h1[data-id="actionbar-heading-mobile"]'
headerDesktop_cat = f'{bar} h3[data-id="actionbar-heading-desktop"]'
headerMobile_cat = f'{bar} h3[data-id="actionbar-heading-mobile"]'
buttonBack = f'{bar} button'
HEADER = 'Help & Support'


@pytest.mark.desktop
def test_header_desktop(sb, homeUrl):
    sb.open(homeUrl)
    sb.assert_text(HEADER, headerDesktop_home)
    sb.assert_element_not_visible(headerMobile_home)
    sb.assert_element_not_visible(buttonBack)


@pytest.mark.mobile
def test_mobile_header_no_back_btn_home(sb, homeUrl):
    sb.open(homeUrl)
    sb.assert_text(HEADER, headerMobile_home)
    sb.assert_element_not_visible(headerDesktop_home)
    sb.assert_element_not_visible(buttonBack)


@pytest.mark.mobile
def test_mobile_header_back_btn_cat_page(sb, catUrl):
    sb.open(catUrl)
    sb.assert_text(HEADER, headerMobile_cat)
    sb.assert_element_not_visible(headerDesktop_cat)
    sb.assert_element_visible(buttonBack)


@pytest.mark.mobile
def test_tap_back_btn(sb, catUrl, homeUrl):
    pytest.xfail("back btn doesn't work with proxy")
    sb.open(catUrl)
    sb.assert_element_visible(buttonBack)
    breakpoint()
    sb.click(buttonBack)
    assert sb.get_current_url() == homeUrl


@pytest.mark.new
def test_header_tags(sb, homeUrl, catUrl, subcatUrl):
    for url in [homeUrl, catUrl, subcatUrl]:
        sb.open(url)
        assert len(sb.find_visible_elements('h1')) == 1
        assert len(sb.find_visible_elements('h3')) >= 1
