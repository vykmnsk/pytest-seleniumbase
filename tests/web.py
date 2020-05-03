def test_web(sb):
	sb.open('http://www.google.com')
	assert 'Google Search' == \
		sb.get_attribute('input[name="btnK"]', 'value')
