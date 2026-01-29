# Define o interpretador e comandos
PYTHON = python3
PIP = pip

install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .
	
test:
	pytest

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name "*.pyc" -delete

all: install test clean