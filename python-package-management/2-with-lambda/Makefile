POETRY ?= poetry
SAM ?= sam

PYTHON_PROJECT_DIR:=python_root

.PHONY: install
install:
	cd ./${PYTHON_PROJECT_DIR} ; \
	$(POETRY) install

.PHONY: build
build: install
	cd ./${PYTHON_PROJECT_DIR} ; \
	$(POETRY) export --without-hashes -f requirements.txt -o requirements.txt --with-credentials ; \
  cd .. ; \
	$(SAM) build

.PHONY: deploy
deploy: build
	$(SAM) deploy --no-confirm-changeset
