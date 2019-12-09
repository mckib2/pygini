
# Remove any existing distribution archives
rm -rf dist

# Generate distribution archives
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

# Upload
python -m pip install --user --upgrade twine
python -m twine upload dist/*
