pytest-seleniumbase
===================
Browser UI test automation framework

setup
----- 

seup virtual environment

	python3 -m venv ./venv
	chmod +x venv/bin/activate
	source venv/bin/activate


install python libs

	pip install --upgrade pip
	pip install -r requirements.txt


install selenium web drivers

	seleniumbase install chromedriver latest
	seleniumbase install firefoxdriver

run
---
Set SuT environment

	export PYTEST_ADDOPTS="--sutenv=[SUT_LABEL]
	--start-page=[SITE_URL]
	--proxy=[SERVER]:[PORT]
	--data=[USERNAME]:[PASSWORD]

	(optionally create .sh files for dev, test, staging, prod in ./env)

Local

	pytest -m "not (mobile or desktop)"  --headless --reuse-session

	pytest -m mobile --browser=chrome --mobile

	pytest -vv --browser=firefox --last-failed -s --pdb

BrowserStack

	pytest -m 'not login' --browser=remote --server=${BROWSERSTACK_USER}:${BROWSERSTACK_ACCESSKEY}@hub.browserstack.com --port=80 --cap_file=remote_caps/bs-ie11.py --maximize-window
