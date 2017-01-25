SHELL = /bin/zsh
SHELLFLAGS = -ilc

PROJECT := $(shell basename $(shell pwd))
WORKON_HOME := $(shell echo $$WORKON_HOME)
VENV_PATH := $(WORKON_HOME)/$(PROJECT)
VENV_BIN_PATH := $(VENV_PATH)/bin

DOCKER_REPO = callforamerica
DOCKER_TAG := $(DOCKER_REPO)/$(PROJECT):latest

.PHONY: init develop publish test build

init:
	@zsh -ilc "mkvirtualenv -a $(PWD) -r requirements.txt -r requirements-test.txt $(PROJECT)"
	@echo -e "\nRemember to execute: workon $(PROJECT)"

develop:
	$(VENV_BIN_PATH)/python3 setup.py develop

publish:
	$(VENV_BIN_PATH)/python3 setup.py register -r pypi
	$(VENV_BIN_PATH)/python3 setup.py sdist upload -r pypi
	rm -rf build dist *.egg-info

test:
	$(VENV_BIN_PATH)/py.test

build:
	@docker build -t $(DOCKER_TAG) --force-rm .
