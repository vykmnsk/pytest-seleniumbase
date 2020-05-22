import pytest
from anytest import retry

searchInput = 'input#search-autocomplete'
searchResult = 'div[role="combobox"]'
PLACEHOLDER = 'Try: "How do I read my bill?"'


def test_search_box(sb):
    box = sb.get_element(searchInput)
    assert PLACEHOLDER == box.get_attribute("placeholder")


@pytest.mark.new
def test_search_results(sb):
    sb.update_text(searchInput, 'bill')

    def assert_resultsDisplayed():
        results = sb.get_element(searchResult)
        assert results.get_attribute('aria-expanded') == 'true'

    retry((assert_resultsDisplayed), 5, 1)
