# VARIABLES

SHELL=./scripts/newshell.sh

# TARGETS
.status/setup_done:
	./scripts/setup.sh


.PHONY: setup
setup: .status/setup_done
	@echo "Done setup"


.PHONY: test
test: 
	python -m unittest