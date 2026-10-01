.PHONY: build test lint run docker-build docker-run

# This Markdown-only repository has no build command.
build:
	@:

test:
	python3 -m unittest discover -s .referee/002-test-evidence-definition -v

# No lint tool or lint configuration is declared by this repository.
lint:
	@:

# There is no application entry point; the documented executable command is the referee test.
run: test

docker-build:
	docker build --tag evidence-definition:local .

docker-run:
	docker run --rm evidence-definition:local
