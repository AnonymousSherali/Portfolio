# Railway.com ga Deploy Qilish - To'liq Yo'riqnoma

Portfolio Django backend loyihasini Railway.com ga deploy qilish bo'yicha qadamma-qadam yo'riqnoma.

## Railway.com Nima?

Railway - zamonaviy cloud platform bo'lib, GitHub bilan avtomatik integratsiya qilingan. Django loyihalarini oson va tez deploy qilish imkonini beradi.

**Afzalliklari:**
- ✅ Bepul tier (500 soatgacha/oyda)
- ✅ PostgreSQL database bepul
- ✅ GitHub bilan avtomatik deploy
- ✅ SSL sertifikat avtomatik
- ✅ Oson sozlash

---

## Boshlash Oldin - Kerakli Fayllar

Barcha kerakli fayllar tayyor qilindi:

### 1. **Procfile** (Root papkada)
```
web: cd backend && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

### 2. **railway.json** (Root papkada)
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "cd backend && python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
  }
}
```

### 3. **runtime.txt** (Root papkada)
```
python-3.11.0
```

### 4. **backend/requirements.txt** (Yangilangan)
```
Django>=5.0,<5.1
djangorestframework>=3.14.0
django-cors-headers>=4.3.0
Pillow>=10.0.0
python-decouple>=3.8
gunicorn>=21.2.0
whitenoise>=6.6.0
psycopg2-binary>=2.9.9
dj-database-url>=2.1.0
```

### 5. **backend/config/settings.py** (Production uchun yangilangan)
- Environment variables qo'llab-quvvatlash
- PostgreSQL database
- Whitenoise static files
- Security settings
- CORS sozlamalari

---

## Qadamma-Qadam Deploy Qilish

### 1. Railway Akkaunt Yaratish

1. **Railway.app ga o'ting:** https://railway.app
2. **"Start a New Project"** yoki **"Login with GitHub"** bosing
3. GitHub akkauntingiz bilan kiring (yoki yangi akkaunt yarating)
4. GitHub integration ni tasdiqlang

---

### 2. Yangi Project Yaratish

1. Railway dashboard da **"New Project"** tugmasini bosing
2. **"Deploy from GitHub repo"** ni tanlang
3. **Portfolio** repositoriyangizni tanlang
4. **Branch:** `claude/django-backend-final-NMUEr` yoki `main` (qaysi birida backend borsa)
5. Railway avtomatik ravishda loyihangizni detect qiladi

---

### 3. PostgreSQL Database Qo'shish

1. Railway project dashboardda **"New"** tugmasini bosing
2. **"Database"** → **"Add PostgreSQL"** ni tanlang
3. PostgreSQL service yaratiladi va avtomatik ravishda `DATABASE_URL` o'rnatiladi
4. Railway avtomatik ravishda backend servicega bog'laydi

---

### 4. Environment Variables Sozlash

Railway dashboardda **Settings** → **Variables** ga o'ting va quyidagilarni qo'shing:

#### **Majburiy Variables:**

```bash
# Django Secret Key (Generate qiling: https://djecrety.ir/)
SECRET_KEY=django-insecure-your-secret-key-here-change-this

# Debug Mode (Production da False)
DEBUG=False

# Allowed Hosts (Railway domain va custom domain)
ALLOWED_HOSTS=*.railway.app,yourdomain.com

# Database URL (Railway avtomatik qo'shadi, tekshiring)
DATABASE_URL=postgresql://...
```

#### **Optional Variables (kerak bo'lsa):**

```bash
# CORS Origins (Agar frontend boshqa domenda bo'lsa)
CORS_ALLOWED_ORIGINS=https://yourfrontend.com,https://yourdomain.com

# Port (Railway avtomatik beradi, o'zgartirmang)
PORT=8000
```

**Muhim:** `DATABASE_URL` ni o'zingiz qo'shmasangiz ham bo'ladi, Railway PostgreSQL qo'shganda avtomatik qo'shadi.

---

### 5. Deploy Qilish

1. Environment variables sozlangandan keyin **"Deploy"** tugmasini bosing
2. Yoki faqat GitHub ga push qiling, Railway avtomatik deploy qiladi:

```bash
git add .
git commit -m "Railway deployment sozlamalari qo'shildi"
git push origin claude/django-backend-final-NMUEr
```

3. Railway build va deploy jarayonini ko'rsatadi:
   - **Building:** Dependencies o'rnatiladi
   - **Deploying:** Migrations run qilinadi
   - **Running:** Gunicorn server ishga tushadi

---

### 6. Build Loglarni Kuzatish

Railway dashboardda:
1. **Deployments** tabini oching
2. Hozirgi deployment ni bosing
3. **Build Logs** va **Deploy Logs** ni ko'ring

Agar xatolik bo'lsa, logs da ko'rinadi.

---

### 7. Migrations Run Qilish

Railway avtomatik ravishda `startCommand` da `migrate` ni run qiladi. Lekin qo'lda ham run qilishingiz mumkin:

Railway dashboardda:
1. **Settings** → **Deploy** ga o'ting
2. **Custom Start Command** maydoniga:
   ```bash
   cd backend && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
   ```
3. **Save** bosing

---

### 8. Superuser Yaratish

Railway CLI orqali yoki Django shell orqali:

#### Usul 1: Railway CLI (Tavsiya)

```bash
# Railway CLI o'rnatish
npm i -g @railway/cli

# Login
railway login

# Project ga connect
railway link

# Shell ochish
railway run python backend/manage.py createsuperuser
```

#### Usul 2: Railway Dashboard (Environment Variables)

1. Temporary script yaratish `backend/create_superuser.py`:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'changethispassword')
    print('Superuser created!')
```

2. `railway.json` da startCommand ga qo'shish:
```json
"startCommand": "cd backend && python manage.py migrate && python create_superuser.py && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
```

---

### 9. Domain va URL

Deploy bo'lgandan keyin Railway sizga URL beradi:

```
https://your-project-name.up.railway.app
```

**URLs:**
- Frontend: `https://your-project-name.up.railway.app/`
- API: `https://your-project-name.up.railway.app/api/`
- Admin: `https://your-project-name.up.railway.app/admin/`

---

### 10. Custom Domain Qo'shish (Optional)

Agar o'z domeningiz bo'lsa:

1. Railway dashboardda **Settings** → **Domains** ga o'ting
2. **"Add Domain"** bosing
3. Domeningizni kiriting: `portfolio.yourdomain.com`
4. DNS sozlamalaringizda CNAME record qo'shing:
   ```
   Type: CNAME
   Name: portfolio
   Value: your-project-name.up.railway.app
   ```
5. SSL avtomatik o'rnatiladi (Let's Encrypt)

---

## Muammolarni Hal Qilish

### ❌ Build Failed

**Sabab:** Dependencies o'rnatilmadi yoki Python versiyasi mos emas.

**Hal:**
1. `requirements.txt` tekshiring
2. `runtime.txt` da to'g'ri Python versiyasi borligini tekshiring
3. Build logs ni o'qing

### ❌ Database Connection Error

**Sabab:** `DATABASE_URL` o'rnatilmagan.

**Hal:**
1. PostgreSQL service qo'shilganligini tekshiring
2. Environment Variables da `DATABASE_URL` borligini tekshiring
3. Settings.py da `dj_database_url` import qilinganligini tekshiring

### ❌ Static Files Yuklanmayapti

**Sabab:** Whitenoise ishlamayapti yoki `collectstatic` run qilinmagan.

**Hal:**
1. `whitenoise` `requirements.txt` da borligini tekshiring
2. Middleware da `WhiteNoiseMiddleware` borligini tekshiring
3. `startCommand` ga `collectstatic` qo'shing:
   ```bash
   cd backend && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
   ```

### ❌ 500 Internal Server Error

**Sabab:** `DEBUG=False` bo'lganda xatoliklar ko'rinmaydi.

**Hal:**
1. Railway logs ni ko'ring: **Deployments** → **View Logs**
2. Temporary `DEBUG=True` qiling (faqat test uchun!)
3. `ALLOWED_HOSTS` ga Railway domain qo'shilganligini tekshiring

### ❌ CSRF Token Error

**Sabab:** HTTPS da CSRF cookies ishlamayapti.

**Hal:**
1. `settings.py` da `CSRF_TRUSTED_ORIGINS` qo'shing:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://yourdomain.com',
]
```

---

## Production Checklist

Deploy qilishdan oldin tekshiring:

- ✅ `DEBUG=False` production da
- ✅ `SECRET_KEY` o'zgartirilgan va xavfsiz
- ✅ `ALLOWED_HOSTS` to'g'ri sozlangan
- ✅ PostgreSQL database qo'shilgan
- ✅ `DATABASE_URL` environment variable bor
- ✅ Static files `collectstatic` orqali to'plangan
- ✅ Migrations run qilingan
- ✅ Superuser yaratilgan
- ✅ CORS sozlamalari to'g'ri (agar frontend boshqa domenda)
- ✅ Media files uchun cloud storage (AWS S3, Cloudinary)

---

## Railway CLI Commands

Foydali CLI commandlar:

```bash
# Login
railway login

# Link to project
railway link

# Logs ko'rish
railway logs

# Environment variables ko'rish
railway vars

# Shell ochish
railway run bash

# Django shell
railway run python backend/manage.py shell

# Database backup
railway run python backend/manage.py dumpdata > backup.json
```

---

## Media Files (Rasmlar)

Railway bepul tierda file storage cheklangan. Production da media files uchun cloud storage ishlatish tavsiya qilinadi:

### AWS S3 (Tavsiya)

1. **django-storages** o'rnatish:
```bash
pip install django-storages boto3
```

2. **settings.py** ga qo'shish:
```python
if not DEBUG:
    # AWS S3 Settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'us-east-1'

    # Media files
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

### Cloudinary (Oson alternative)

```bash
pip install cloudinary django-cloudinary-storage
```

---

## Monitoring va Logs

Railway dashboard da:
- **Metrics:** CPU, Memory, Network usage
- **Logs:** Real-time logs ko'rish
- **Deployments:** Deploy history
- **Settings:** Variables, Domains, Build settings

---

## Narxlar (2024)

Railway pricing:

- **Hobby Plan (Free):**
  - $5 credit/oyda
  - 500 hours runtime
  - 1 GB RAM
  - PostgreSQL included

- **Pro Plan ($20/oy):**
  - Unlimited projects
  - 8 GB RAM
  - Priority support

Bepul tier kichik loyihalar uchun kifoya!

---

## Qo'shimcha Resurslar

- Railway Documentation: https://docs.railway.app
- Django Deployment Checklist: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
- Railway Discord: https://discord.gg/railway

---

## Xulosa

Railway.com ga deploy qilish juda oson:

1. ✅ GitHub repository bog'lash
2. ✅ PostgreSQL qo'shish
3. ✅ Environment variables sozlash
4. ✅ Deploy tugmasini bosish

Va sizning Django backend live bo'ladi! 🚀

Muammolar bo'lsa, Railway logs va dokumentatsiyani tekshiring.

**Omad yor bo'lsin!** 🎉
