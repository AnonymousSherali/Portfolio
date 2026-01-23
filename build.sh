#!/usr/bin/env bash
# Railway build script

set -e  # Exit on error

echo "====== Running migrations ======"
python manage.py migrate --noinput

echo "====== Creating superuser ======"
python manage.py create_default_superuser

echo "====== Collecting static files ======"
python manage.py collectstatic --noinput --clear

echo "====== Build complete ======"
