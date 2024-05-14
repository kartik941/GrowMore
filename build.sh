#!/usr/bin/env bash
# Exit on error .
set -o errexit
pip install wheel
# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

python manage.py collectstatic --no-input


