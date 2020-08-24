# shell with environment
preaction()
{
	if [  -f "./venv/bin/activate" ]; then
			. ./venv/bin/activate
	fi
}

postaction()
{
	if [  -f "./venv/bin/activate" ]; then
			deactivate 2> /dev/null || true
	fi	
}

preaction && /bin/bash "$@" && postaction
