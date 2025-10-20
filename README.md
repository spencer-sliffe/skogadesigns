# SkogaDesigns

E-commerce site for jewelry, built with:

- **Backend**: Django 5 + Django REST Framework (DRF)
- **Frontend**: Next.js (App Router, TypeScript, Tailwind)
- **Infra**: WSL2 (Ubuntu) + VS Code, Postgres (Neon/Supabase), Cloudflare R2 for assets

---

## Quick Start (Local Dev)

```bash
cd ~/code
git clone git@github.com:spencer-sliffe/skogadesigns.git
cd skogadesigns

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel setuptools

pip install -r backend/requirements.txt

cd frontend
npm install
cd ..

cp backend/.env.example backend/.env
python manage.py migrate
```

---

## Running the stack

Open two terminals:

**Backend**
```bash
./scripts/dev.sh backend
```

**Frontend**
```bash
./scripts/dev.sh frontend
```

Backend → http://localhost:8000  
Frontend → http://localhost:3000

---

## Structure

```
skogadesigns/
├─ backend/        # Django project & apps
├─ frontend/       # Next.js app
├─ scripts/        # helper dev scripts
├─ .editorconfig
├─ .gitattributes
├─ .gitignore
└─ README.md
```

---

## Environments

- Local: `backend/.env`
- Production: environment variables via host

---

## Common Commands

**Backend**
```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Frontend**
```bash
cd frontend
npm run dev
npm run build
npm start
```

---

## Pull Request Workflow

All changes must be proposed through a feature branch and reviewed via pull request before merging into `main`.

### Branch Naming Convention
```
<project-code>/<short-description>

Example:
sd-008/add-field-permissions
```

### Pull Request Template
```
### Summary
Briefly describe what the PR does.

### Details
- What was added or changed
- Why it was necessary
- Any migration or setup notes

### Testing
Steps to verify the changes locally.
```

### Steps
```bash
# Create and switch to feature branch
git checkout -b sd-008/add-field-permissions

# Stage and commit changes
git add -A
git commit -m "SD-008: add read and write field permissions"

# Push to origin
git push origin sd-008/add-field-permissions

# Open PR on GitHub
# Title example:
# SD-008: Add read and write field permissions
```

All pull requests must pass tests and be reviewed before merge.
