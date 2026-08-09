# SkillConnect Backend

Production-oriented Django REST backend for **SkillConnect**, a career platform focused on job discovery, profile building, and AI-assisted career tools.

## Project Snapshot

- **Type:** Backend API service (Django + DRF)
- **Domain:** Career platform / Job marketplace
- **Auth:** JWT-based authentication
- **Database:** MySQL (default), supports `DATABASE_URL`-based configuration
- **API Docs:** Swagger + ReDoc (when `drf_yasg` is installed)

## Key Highlights

- Secure account flows: registration, login, profile, password reset
- Job listing and job application APIs
- Career profile modules: experience, education, skills
- Newsletter subscription and contact APIs
- AI endpoints for resume analysis, job match, and interview feedback
- Static asset pipeline with WhiteNoise and collectstatic support
- Cloudinary-ready media storage for production

## Tech Stack

- Python 3.x
- Django 4.2
- Django REST Framework
- SimpleJWT
- MySQL / `dj-database-url`
- WhiteNoise
- Cloudinary
- drf-yasg (API documentation)

## Repository Structure

```text
skillconnect-backend/
├── core/                 # project settings, root urls, AI routes
├── accounts/             # auth + profile domain
├── jobs/                 # jobs + applications domain
├── newsletter/           # subscribe/contact domain
├── resumes/              # resume-related features
├── templates/            # server templates
├── manage.py
├── requirements.txt
└── build.sh
```

## API Surface (Core)

Base path: `/api/`

### Accounts (`/api/accounts/`)
- `POST register/`
- `POST login/`
- `GET/PUT profile/`
- `POST forgot-password/`
- `POST reset-password/`
- `GET/POST experience/`, `PUT/DELETE experience/<id>/`
- `GET/POST education/`, `PUT/DELETE education/<id>/`
- `GET/POST skills/`, `PUT/DELETE skills/<id>/`

### Jobs (`/api/jobs/`)
- `GET /` (list jobs)
- `GET <id>/` (job details)
- `GET categories/`, `GET stats/`
- `POST apply/`
- `POST <job_id>/apply/`
- `GET applications/`, `GET/PUT/DELETE applications/<id>/`

### Newsletter (`/api/newsletter/`)
- `POST subscribe/`
- `POST contact/`

### AI (`/api/ai/`)
- `POST analyze-resume/`
- `POST demo-analysis/`
- `POST job-match/`
- `POST interview-feedback/`

### Documentation Endpoints
- `/api/docs/` (Swagger UI)
- `/api/redoc/` (ReDoc)
- `/api/schema.json`

## Local Setup

```bash
# 1) Clone
git clone https://github.com/nijamuddin-mujawar/skillconnect-backend.git
cd skillconnect-backend

# 2) Create virtual env
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run migrations
python manage.py migrate

# 5) Start server
python manage.py runserver
```

## Build & Validation

```bash
# Build script used for deployment-style validation
bash build.sh

# Test command (set DATABASE_URL for local sqlite testing if needed)
DATABASE_URL=sqlite:///tmp/temp.db python manage.py test
```

## Deployment Notes

- `build.sh` installs dependencies and runs `collectstatic`
- Production entrypoint is supported via `Procfile` / `start.sh`
- Configure environment variables for secret keys, database, and cloud media

## Resume-Ready Contribution Summary

Built and maintained a Django REST backend powering a career platform with authentication, job workflows, profile systems, and AI-assisted features; integrated production concerns including static asset optimization, cloud media storage, and API documentation.

## Contact

**Nijamuddin Mujawar**
- GitHub: https://github.com/nijamuddin-mujawar
- Email: nijamujawar@gmail.com

