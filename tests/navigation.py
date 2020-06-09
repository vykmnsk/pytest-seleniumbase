import pytest
from anytest import retry, TIMEOUT_MED, TIMEOUT_MAX
from home import tileImages
from search import searchPickTop
from random import randrange


firstAccordion = '[data-id="accordion-group-0"]'
firstArticleLink = '[data-id="subcategory-page-article-list0"]'
TEXT_ALL_ARTICLES = 'Show all articles'

cssCrumbs = 'ol.MuiBreadcrumbs-ol'
cssCrumbLinks = f'{cssCrumbs} li.MuiBreadcrumbs-li a'

articleScreen = '[data-id="article"]'
articleFeedback = '[data-id="feedback-label"]'
articleBtnYes = '[data-id="yes"]'
articleBtnNo = '[data-id="no"]'
FEEDBACK_THANKS = 'Thanks for your feedback!'


def test_check_all_page_types_headers(sb):
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


def test_article_feedback(sb, homeUrl):
    searchPickTop(sb, 'how')
    assert_onArticlePage(sb)
    sb.assert_element_visible(articleBtnYes)
    sb.assert_element_visible(articleBtnNo)
    btns = [articleBtnYes, articleBtnNo]
    pick = randrange(len(btns))
    print(f'clicking {btns[pick]}')
    sb.click(btns[pick])
    sb.assert_text_visible(FEEDBACK_THANKS)


@pytest.mark.desktop
def test_nav_back_from_article(sb, homeUrl):
    searchPickTop(sb, 'how')

    assert_onArticlePage(sb)
    sb.assert_element_visible(cssCrumbs)
    crumbLinks3 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks3) == 3
    crumbLinks3[-1].click()

    assert_onSubcatPage(sb)
    sb.assert_element_visible(cssCrumbs)
    crumbLinks3 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks3) == 3
    crumbLinks3[-2].click()

    assert_onCatPage(sb)
    sb.assert_element_visible(cssCrumbs)
    crumbLinks2 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks2) == 2
    crumbLinks2[-2].click()

    assert_onHomePage(sb, homeUrl)
    crumbLinks0 = sb.find_elements(cssCrumbLinks)
    assert len(crumbLinks0) == 0


# --- helper funcs ----------------
def assert_onHomePage(sb, homeUrl):
    assert sb.get_current_url() in homeUrl


def assert_onCatPage(sb):
    sb.assert_element_visible(firstAccordion)


def assert_onSubcatPage(sb):
    sb.assert_element_visible(firstArticleLink)


def assert_onArticlePage(sb):
    sb.assert_element_visible(articleScreen)
    sb.assert_element_visible(articleFeedback)


def openCategoryPage(sb):
    sb.click(tileImages)
    assert_onCatPage(sb)


def openSubcategoryPage(sb):
    sb.click(firstAccordion)

    def waitForArticleLinks():
        vlinks = sb.find_visible_elements('a')
        alinks = [vl for vl in vlinks if vl.text.startswith(TEXT_ALL_ARTICLES)]
        assert len(alinks) > 0
        return alinks

    alinks = retry(waitForArticleLinks, 10, 1)
    alinks[-1].click()
    assert_onSubcatPage(sb)


def openArticlePage(sb):
    sb.click(firstArticleLink)
    assert_onArticlePage(sb)
