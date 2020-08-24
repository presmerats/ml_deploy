#!/bin/bash
source scripts/config.sh
# setup environment
setup_pyenv() {
	ENVIRONMENT="$PROJECT_NAME_env"
	pyenv install 3.7.2 -s
	pyenv virtualenv 3.7.2 $ENVIRONMENT -f
	pyenv local $ENVIRONMENT
	pip install -r requirements.txt
	pip install jupyter
	python -m ipykernel install --user
}



# setup venv version
setup_venv() {
	set -e
	mkdir -p .status
	mkdir -p doc
	mkdir -p data
	mkdir -p src/$PROJECT_NAME
	mkdir -p notebooks
	rm -rf ./venv/
	python3 -m venv venv
}


# intall
setup_packages() {
	pip install -r requirements.txt
	if [ -f src/setup.y ]; then
	   cd src && pip install -e .
        fi
}

# setup ipython kernel
jupyter_kernel() {
	ipython kernel install --user --name="$PROJECT_NAME"
	touch ./venv/.jupyter_set
}


setup_venv
setup_packages
jupyter_kernel
touch .status/setup_done


