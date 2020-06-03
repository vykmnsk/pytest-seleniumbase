import pytest
from anytest import retry
from random import randrange

searchInput = 'input#search-autocomplete'
searchResult = 'div[role="combobox"]'
searchResults = ".search-result-list li"
PLACEHOLDER = 'Try: "How do I read my bill?"'


def test_search_box(sb):
    box = sb.get_element(searchInput)
    assert PLACEHOLDER == box.get_attribute("placeholder")


def test_search_results_display_3(sb):
    results = search(sb, 'bill')
    assert len(results) == 3


@pytest.mark.parametrize('criteria', ['pay', 'bill', 'meter', 'solar'])
def test_find_article(sb, criteria):
    results = search(sb, criteria)
    pick = randrange(len(results))
    result = results[pick]
    articleFound = result.text
    result.click()
    pageTitle = sb.get_text('h1')
    assert articleFound in pageTitle


def search(sb, criteria):
    def assert_resultsDisplayed():
        results = sb.get_element(searchResult)
        assert results.get_attribute('aria-expanded') == 'true'
    
    sb.update_text(searchInput, criteria)
    retry((assert_resultsDisplayed), 6, 1)
    return sb.find_elements(searchResults)

