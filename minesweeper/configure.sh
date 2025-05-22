#!/usr/bin/env bash

if [ ! -d .venv ]; then
    python -m venv .venv
fi

echo "Activating virtual environment"
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

