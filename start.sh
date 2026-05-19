#!/usr/bin/env bash

set -o errexit

echo "🔄 Running database migrations..."
python manage.py migrate --no-input

echo "👤 Creating admin user (if not exists)..."
python create_admin.py || echo "Admin already exists"

echo "💼 Adding sample jobs (if not exists)..."
python add_jobs.py || echo "Jobs already exist"

echo "🚀 Starting Gunicorn server..."
PORT=${PORT:-8080}
exec gunicorn core.wsgi:application --timeout 120 --workers 2 --threads 2 --bind 0.0.0.0:$PORT
