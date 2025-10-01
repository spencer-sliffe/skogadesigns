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
