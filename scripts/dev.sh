#!/usr/bin/env bash
set -euo pipefail
if [[ -f ".venv/bin/activate" ]]; then source .venv/bin/activate; fi
case "${1:-}" in
  backend)
    cd backend
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
    ;;
  frontend)
    cd frontend
    npm install
    npm run dev
    ;;
  *)
    echo "Usage: scripts/dev.sh [backend|frontend]"
    ;;
esac
