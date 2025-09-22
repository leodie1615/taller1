#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install ipykernel
python -m ipykernel install --user --name=taller1-env --display-name "Python (taller1-env)"
