#!/usr/bin/env bash
# Railway build script.
#
# Only build-time work belongs here. Migrations and superuser creation run at
# start-up instead (see release.sh) because the build image is discarded and
# the database lives in a separate service.

set -e

echo "====== Collecting static files ======"
python manage.py collectstatic --noinput --clear

echo "====== Build complete ======"
