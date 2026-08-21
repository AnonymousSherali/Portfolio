#!/usr/bin/env bash
# Runtime start script for Railway.
#
# Migrations run here rather than during the build so they are applied against
# the live database service. Both commands are idempotent, so it is safe for
# this to run on every restart.

set -e

echo "====== Running migrations ======"
python manage.py migrate --noinput

echo "====== Ensuring superuser exists ======"
python manage.py create_default_superuser

echo "====== Starting gunicorn ======"
exec gunicorn config.wsgi:application \
    --bind "0.0.0.0:${PORT:-8000}" \
    --workers "${WEB_CONCURRENCY:-2}" \
    --threads 4 \
    --timeout 120 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
