# Railway Deployment Guide

## Environment Variables

Railway dashboardda quyidagi environment variables'larni o'rnatish kerak:

### Required Variables:

1. **SECRET_KEY** (Django secret key)
   ```
   django-insecure-YOUR-RANDOM-SECRET-KEY-HERE
   ```

2. **DEBUG** (Production uchun False)
   ```
   False
   ```

3. **ALLOWED_HOSTS** (Auto-generated, Railway o'zi qo'shadi)
   ```
   portfolio-production-f3aa.up.railway.app
   ```

## Deployment Steps

1. **Railway Dashboard -> Environment Variables:**
   - Add `SECRET_KEY` variable
   - Add `DEBUG=False` variable

2. **Railway automatically runs:**
   ```bash
   pip install -r requirements.txt
   python manage.py collectstatic --noinput
   python manage.py migrate
   gunicorn config.wsgi --bind 0.0.0.0:$PORT
   ```

3. **Create superuser (via Railway CLI):**
   ```bash
   railway run python manage.py createsuperuser
   ```

## Post-Deployment

1. Navigate to: `https://portfolio-production-f3aa.up.railway.app/admin/`
2. Login with your superuser credentials
3. Add your portfolio data:
   - Profile
   - Services
   - Timeline entries (Education & Experience)
   - Skills
   - Project categories
   - Projects
   - Testimonials
   - Clients
   - Blog posts

## Important Notes

- Railway uses ephemeral filesystem, so uploaded media files will be lost on restart
- For persistent media storage, use:
  - Cloudinary
  - AWS S3
  - Railway Volumes (if available)

## Troubleshooting

If site doesn't load:
1. Check Railway logs
2. Verify environment variables are set
3. Ensure migrations ran successfully
4. Check ALLOWED_HOSTS in settings.py
