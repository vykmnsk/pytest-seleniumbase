import pytest
from anytest import retry, TIMEOUT_MED, TIMEOUT_MAX
from home import tileImages


firstAccordion = '[data-id="accordion-group-0"]'
firstArticle = '[data-id="subcategory-page-article-list0"]'
TEXT_ALL_ARTICLES = 'Show all articles'

cssCrumbs = 'ol.MuiBreadcrumbs-ol'
cssCrumbLinks = f'{cssCrumbs} li.MuiBreadcrumbs-li a'

articleFeedback = '[data-id="feedback-label"]'


def openCategoryPage(sb):
    sb.click(tileImages)
    sb.assert_element_visible(firstAccordion)


def openSubcategoryPage(sb):
    sb.click(firstAccordion)

    def waitForArticleLinks():
        vlinks = sb.find_visible_elements('a')
        alinks = [vl for vl in vlinks if vl.text.startswith(TEXT_ALL_ARTICLES)]
        assert len(alinks) > 0
        return alinks

    alinks = retry(waitForArticleLinks, 3, 1)
    alinks[-1].click()
    sb.assert_element_visible(firstArticle)


def openArticlePage(sb):
    sb.click(firstArticle)
    sb.assert_element_visible(articleFeedback)


def test_check_page_headers(sb):
    def assert_headerStructure():
        assert len(sb.find_visible_elements('h1')) == 1
        assert len(sb.find_visible_elements('h3')) >= 1

    assert_headerStructure()
    openCategoryPage(sb)
    assert_headerStructure()
    openSubcategoryPage(sb)
    assert_headerStructure()
    openArticlePage(sb)
    assert_headerStructure()


@pytest.mark.desktop
def test_nav_to_from_subcat(sb, homeUrl):
    openCategoryPage(sb)
    openSubcategoryPage(sb)

    sb.assert_element_visible(cssCrumbs)
    crumbLinks3 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks3) == 3
    crumbLinks3[1].click()

    sb.assert_element_visible(firstAccordion)
    sb.assert_element_visible(cssCrumbs)
    crumbLinks2 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks2) == 2
    crumbLinks2[0].click()

    assert sb.get_current_url() in homeUrl
    crumbLinks0 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks0) == 0


