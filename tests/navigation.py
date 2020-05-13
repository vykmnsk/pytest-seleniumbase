import pytest
from anytest import retry, TIMEOUT_MED, TIMEOUT_MAX

catId = 'account'
subCatId = 'account-balance'
# subCatName = 'Account balance'
subCatName = 'account-balance'

cssTile = f'a[href="/help-support/{catId}"] div.QuickLinkContainer'
cssAccordion = f'div[label="{subCatName}"]'
TEXT_ALL_ARTICLES = 'Show all articles'

cssCrumbs = 'ol.MuiBreadcrumbs-ol'
cssCrumbLinks = f'{cssCrumbs} li.MuiBreadcrumbs-li a'


def test_nav_to_subcat(sb, homeUrl):
    sb.open(homeUrl)
    sb.get_element(cssTile).click()
    assert (sb.get_current_url().endswith(catId))

    sb.get_element(cssAccordion, timeout=TIMEOUT_MED).click()

    def waitForLinks():
        vlinks = sb.find_visible_elements('a')
        alinks = [vl for vl in vlinks if vl.text.startswith(TEXT_ALL_ARTICLES)]
        assert len(alinks) > 0
        return alinks

    alinks = retry(waitForLinks, 3, 1)
    alinks[-1].click()
    assert (sb.get_current_url().endswith(subCatId))


@pytest.mark.desktop
def test_nav_back_from_subcat(sb, homeUrl):
    sb.open(homeUrl + f'{catId}/{subCatId}')

    sb.assert_element_visible(cssCrumbs)
    crumbLinks3 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks3) == 3
    crumbLinks3[1].click()

    assert (sb.get_current_url().endswith(catId))
    sb.assert_element_visible(cssCrumbs)
    crumbLinks2 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks2) == 2
    crumbLinks2[0].click()

    assert sb.get_current_url() in homeUrl
    crumbLinks0 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks0) == 0
