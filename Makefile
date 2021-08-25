- create_venv: 
	python3 -m venv ./myvenv

- install: requirements.txt
	pip install -r requirements.txt

- test:
	pytest tests/test_code.py

- clean:
	rm -rf __pycache__ */__pycache__ myvenv

- all: create_venv install test clean