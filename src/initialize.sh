#!/bin/bash

if [ ! -d ".venv" ]; then
    if ! pip list | gpip rep -q virtualenv; then
        echo "Detected missing virtualenv lib, installing it"
        pip install virtualenv
        # NOTE: This could not work in all linux distros, check the output for further details
    fi
    echo "Detected missing virtualenv, creating it"
    python -m venv .venv
fi

source .venv/bin/activate

if ! python -c "import borb" &> /dev/null; then
    echo "Detected missing borb lib, installing it"
    pip install borb
fi