#!/usr/bin/env bash
set -euo pipefail

source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 app:app
