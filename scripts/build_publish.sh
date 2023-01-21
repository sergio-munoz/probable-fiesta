#! /bin/bash

rm -rf dist/*
python3 -m pip uninstall probale-fiesta
#vim pyproject.toml
python3 -m build
python3 -m twine upload --repository testpypi dist/* --verbose
python3 -m pip install probale-fiesta
