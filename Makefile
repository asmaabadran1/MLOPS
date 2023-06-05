install:
	pip install -r requirements.txt

lint:
	pylint main.py

test:
	python -m pytest -vv 

deploy:
	uvicorn main_app:app
