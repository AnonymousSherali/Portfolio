# Railway Deployment Guide

## 1. Attach a PostgreSQL database (required)

Railway containers have an **ephemeral filesystem** — the SQLite file is
recreated on every deploy, so everything entered in the admin (profile,
projects, blog posts, even the superuser) disappears on the next push.

In the Railway dashboard: **New → Database → Add PostgreSQL**.

Railway injects `DATABASE_URL` automatically and the app picks it up. No code
changes needed. Without it the app falls back to SQLite, which is fine locally
but loses data on Railway.

## 2. Set environment variables

**Settings → Variables → Raw Editor:**

```env
SECRET_KEY=<paste a 50+ character random key>
DEBUG=False
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=you@example.com
DJANGO_SUPERUSER_PASSWORD=<a strong password>
```

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

If `DJANGO_SUPERUSER_USERNAME` / `DJANGO_SUPERUSER_PASSWORD` are missing, the
start-up script skips superuser creation and logs a warning — no account with a
guessable default password is ever created on a public site.

### Optional variables

| Variable | Default | Purpose |
|---|---|---|
| `ALLOWED_HOSTS` | `.railway.app,localhost,127.0.0.1` | Comma-separated extra hosts |
| `CSRF_TRUSTED_ORIGINS` | `https://*.railway.app` | Comma-separated origins |
| `CORS_ALLOWED_ORIGINS` | *(empty)* | Extra exact origins for the API |
| `MEDIA_ROOT` | `<project>/media` | Point at a mounted volume to keep uploads |
| `WEB_CONCURRENCY` | `2` | Gunicorn worker count |
| `SECURE_SSL_REDIRECT` | `True` | Set `False` only if terminating TLS elsewhere |
| `LOG_LEVEL` | `INFO` | Root log level |
| `TIME_ZONE` | `UTC` | e.g. `Asia/Tashkent` |

## 3. Deployment lifecycle

| Phase | Command | What runs |
|---|---|---|
| Build | `./build.sh` | `collectstatic` only |
| Start | `./release.sh` | `migrate` → `create_default_superuser` → `gunicorn` |

Migrations run at **start-up**, not build time, so they are applied to the live
PostgreSQL service rather than a throwaway build container. Both commands are
idempotent and safe to repeat on every restart.

Healthcheck path is `/health/`, which returns JSON without touching the
database or rendering a template.

## 4. Uploaded images

`MEDIA_ROOT` also lives on the ephemeral filesystem. Pick one:

- **Railway volume** — mount one and set `MEDIA_ROOT` to its path.
- **Cloud storage** — add `django-storages` with S3 or Cloudinary.
- **Do nothing** — re-upload images after each deploy (fine while iterating).

The site renders correctly either way: every template guards missing images
with `{% if %}` and falls back to a bundled placeholder.

## 5. After the first successful deploy

1. Open `https://<your-domain>/admin/` and sign in.
2. Fill in **Profile** first — the sidebar, About and Contact sections read from it.
3. Add Services, Timeline entries, Skills, Project categories, Projects,
   Testimonials, Clients and Blog posts as needed.
4. Empty sections simply render empty; nothing breaks if you skip one.

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export DEBUG=True
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Run the test suite:

```bash
DEBUG=True python manage.py test portfolio
```

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Admin data vanishes after a deploy | No PostgreSQL attached | Step 1 |
| Cannot log in to admin | Superuser env vars not set | Step 2, then redeploy |
| `DisallowedHost` error | Custom domain | Add it to `ALLOWED_HOSTS` |
| CSRF failure on the admin login form | Custom domain | Add `https://<domain>` to `CSRF_TRUSTED_ORIGINS` |
| Healthcheck fails | App crashed on start | Read the deploy logs — `release.sh` echoes each step |
| Images 404 | Uploads wiped by a deploy | See step 4 |
