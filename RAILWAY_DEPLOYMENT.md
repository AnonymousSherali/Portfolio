# Railway Deployment Guide - Portfolio Project

## 🚀 Quick Setup

### Step 1: Set Environment Variables in Railway

Railway Dashboard → Settings → Variables → Add the following:

**REQUIRED (Xavfsizlik uchun muhim):**
```env
SECRET_KEY=<generate-random-key>
DEBUG=False
```

**OPTIONAL (Superuser uchun - tavsiya etiladi):**
```env
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=YourStrongPassword123!
```

### Generate SECRET_KEY

Terminal'da quyidagi commandni ishga tushiring:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Natijani Railway'dagi `SECRET_KEY` variable'ga joylashtiring.

---

## 📋 Deployment Process

Railway avtomatik quyidagilarni bajaradi:

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Collect static files:** `python manage.py collectstatic --noinput`
3. **Run migrations:** `python manage.py migrate`
4. **Create superuser:** `python manage.py create_default_superuser` (agar environment variables o'rnatilgan bo'lsa)
5. **Start server:** `gunicorn config.wsgi`

---

## ✅ Deployment Success Check

### 1. Railway Logs tekshirish:
Railway Dashboard → Deployments → Latest Deployment → View Logs

**Quyidagilarni topish kerak:**
```
✓ Migrations completed
✓ Successfully created superuser "admin"
✓ Static files collected
✓ Gunicorn started
```

### 2. Admin Panel tekshirish:
```
https://portfolio-production-f3aa.up.railway.app/admin/login/
```

**Kirish uchun:**
- Username: `DJANGO_SUPERUSER_USERNAME` (default: admin)
- Password: `DJANGO_SUPERUSER_PASSWORD` (default: admin123)

---

## 🔧 Troubleshooting

### ❌ Agar admin panelga kira olmasangiz:

**1. Railway Logs'ni tekshiring:**
```
Railway Dashboard → Deployments → View Logs
```

**2. Environment Variables tekshiring:**
```
Railway Dashboard → Settings → Variables
```
Quyidagilar mavjudligini tekshiring:
- ✅ SECRET_KEY
- ✅ DJANGO_SUPERUSER_USERNAME
- ✅ DJANGO_SUPERUSER_PASSWORD
- ✅ DJANGO_SUPERUSER_EMAIL

**3. Agar superuser yaratilmagan bo'lsa:**

Railway Console orqali:
```bash
python manage.py create_default_superuser
```

Yoki interaktiv:
```bash
python manage.py createsuperuser
```

**4. Agar static fayllar yuklanmasa:**
```bash
python manage.py collectstatic --noinput
```

**5. Railway'ni qayta deploy qiling:**
```
Railway Dashboard → Deployments → Redeploy
```

---

## 📝 Post-Deployment: Portfolio Data qo'shish

Admin panelga kirganingizdan keyin quyidagi ma'lumotlarni to'ldiring:

### 1. Profile (Shaxsiy ma'lumotlar)
- ✏️ Name, Title, Bio
- ✏️ Email, Phone, Birthday, Location
- ✏️ Avatar image
- ✏️ Social media links (Facebook, Twitter, Instagram, LinkedIn, GitHub)

### 2. Services (Xizmatlar)
- ✏️ Service name
- ✏️ Description
- ✏️ Icon/Image

### 3. Timeline Entries (Ta'lim va Ish Tajribasi)
- ✏️ Education entries (Type: Education)
- ✏️ Experience entries (Type: Experience)
- ✏️ Institution, Title, Description, Dates

### 4. Skills (Ko'nikmalar)
- ✏️ Skill name
- ✏️ Proficiency percentage (0-100)
- ✏️ Category

### 5. Project Categories
- ✏️ Category name (Web Design, Applications, etc.)

### 6. Projects
- ✏️ Title, Description
- ✏️ Project image
- ✏️ Category selection
- ✏️ Live URL, GitHub URL
- ✏️ Technologies used

### 7. Testimonials (Mijozlar fikrlari)
- ✏️ Client name
- ✏️ Client avatar
- ✏️ Testimonial content

### 8. Clients (Mijozlar logotipi)
- ✏️ Client name
- ✏️ Logo image
- ✏️ Website URL

### 9. Blog Posts
- ✏️ Title, Content, Excerpt
- ✏️ Featured image
- ✏️ Category, Published date

---

## ⚠️ Important Notes

### Media Files (Rasmlar)
Railway ephemeral filesystem ishlatadi - server restart bo'lsa rasmlar yo'qoladi.

**Yechim:** Cloud storage ishlatish
- Cloudinary (Free tier: 25GB)
- AWS S3
- Railway Volumes

### Database
Hozirda SQLite ishlatilmoqda. Production uchun PostgreSQL tavsiya etiladi.

**Railway PostgreSQL qo'shish:**
1. Railway Dashboard → New → Database → PostgreSQL
2. Environment variables avtomatik qo'shiladi
3. settings.py'ni PostgreSQL uchun sozlang

---

## 🎯 Final Checklist

- ✅ Railway environment variables o'rnatilgan
- ✅ Deployment successful (logs'da xatolik yo'q)
- ✅ Admin panelga kirildi
- ✅ Superuser yaratilgan
- ✅ Static files ishlayapti (CSS/JS yuklanmoqda)
- ✅ Portfolio ma'lumotlari qo'shilgan
- ✅ Frontend sahifa to'g'ri ko'rsatilmoqda

---

## 📞 Support

Muammo bo'lsa:
1. Railway logs'ni tekshiring
2. Browser console (F12) xatolarni tekshiring
3. Environment variables to'g'riligini tasdiqlang
4. Redeploy qilib ko'ring
