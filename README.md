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
	pytest tests/* -v -m "not (mobile or desktop)" --sutenv=staging --headless --reuse-session

	pytest tests/* -v -m mobile --browser=chrome --mobile

	pytest tests/* -vv --browser=firefox --lf -s --pdb
