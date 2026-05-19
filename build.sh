#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

DATABASE_URL="sqlite:///tmp/temp.db" python manage.py collectstatic --no-input --clear

echo "✅ Build complete. Migrations will run at startup."
