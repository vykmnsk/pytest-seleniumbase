import pytest
from anytest import TIMEOUT_MED

appHome = '[data-id="home"]'
headerHome = 'h2[data-id="title"]'
tileContainer = 'div[data-id="quicklink-container"]'
tileImages = f'{tileContainer} svg'

headerHomeDesktop = 'h1[data-id="actionbar-heading-desktop"]'

HEADER_SITE = 'Help & Support'
HEADER_HOME = 'What can we help you with?'


def test_site_loaded(sb):
    # sb.assert_no_404_errors()
    sb.assert_element(appHome)
    pageTitle = sb.get_title()
    assert HEADER_SITE in pageTitle
    assert HEADER_HOME in pageTitle


def test_search_header(sb):
    headers = sb.find_visible_elements(headerHome)
    assert len(headers) == 1 #one is hidden
    assert headers[0].text == HEADER_HOME


@pytest.mark.desktop
def test_home_page_headers(sb):
    sb.assert_text(HEADER_SITE, headerHomeDesktop, timeout=TIMEOUT_MED)


def test_tiles_count(sb):
    sb.assert_element(tileContainer, timeout=TIMEOUT_MED)
    tiles = sb.find_elements(tileImages)
    assert len(tiles) == 8


@pytest.mark.skip
def test_tiles_not_same(sb):
    sb.assert_element(tileContainer, timeout=TIMEOUT_MED)
    imgLabels = [
        e.get_attribute('data-id')
        for e in sb.find_elements(tileImages)]
    uniqImagesCount = len(set(imgLabels))
    assert uniqImagesCount == 8


@pytest.mark.desktop
def test_header_desktop(sb):
    searchDescr = sb.get_element('div[data-id="description"]').text
    assert len(searchDescr) <= 100


