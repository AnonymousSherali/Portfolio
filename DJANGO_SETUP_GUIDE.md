# Django Portfolio - To'liq Sozlash Yo'riqnomasi

Portfolio dizayni Django backend bilan to'liq integratsiya qilindi!

## Fayl Strukturasi

```
Portfolio/
├── backend/                              # Django backend
│   ├── config/                          # Django sozlamalari
│   │   ├── settings.py                  # Asosiy sozlamalar
│   │   └── urls.py                      # Asosiy URL config
│   ├── portfolio/                       # Portfolio app
│   │   ├── templates/                   # Django templates
│   │   │   └── portfolio/
│   │   │       └── index.html          # Asosiy sahifa (Django template)
│   │   ├── static/                      # Static fayllar
│   │   │   └── portfolio/
│   │   │       ├── css/
│   │   │       │   └── style.css       # Portfolio CSS
│   │   │       ├── js/
│   │   │       │   ├── script.js       # Portfolio JS
│   │   │       │   └── api-example.js  # API integration misollari
│   │   │       └── images/              # Barcha rasmlar
│   │   ├── models.py                    # Database modellari
│   │   ├── views.py                     # Views (API + Template)
│   │   ├── serializers.py               # DRF serializers
│   │   └── admin.py                     # Admin konfiguratsiya
│   ├── manage.py                        # Django management
│   └── requirements.txt                 # Python dependencies
├── assets/                              # Original assets (archive)
├── index.html                           # Original HTML (archive)
└── README.md
```

## URL Strukturasi

### Frontend
- `http://localhost:8000/` - Portfolio asosiy sahifasi (Django template)
- `http://localhost:8000/home/` - Portfolio sahifa (alternative)

### Backend API
- `http://localhost:8000/api/profile/` - Profil ma'lumotlari
- `http://localhost:8000/api/services/` - Xizmatlar
- `http://localhost:8000/api/timeline/` - Ta'lim va tajriba
- `http://localhost:8000/api/skills/` - Ko'nikmalar
- `http://localhost:8000/api/projects/` - Loyihalar
- `http://localhost:8000/api/testimonials/` - Sharhlar
- `http://localhost:8000/api/clients/` - Mijozlar
- `http://localhost:8000/api/blog/` - Blog postlar
- `http://localhost:8000/api/contact/` - Kontakt forma (POST)

### Admin Panel
- `http://localhost:8000/admin/` - Django admin

## Tezkor Boshlash

### 1. Virtual Environment va Dependencies

```bash
cd backend

# Virtual environment yaratish
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows

# Dependencies o'rnatish
pip install -r requirements.txt
```

**requirements.txt:**
- Django 5.0
- Django REST Framework 3.14
- django-cors-headers 4.3
- Pillow 10.0

### 2. Database Setup

```bash
# Migratsiyalar yaratish
python manage.py makemigrations

# Database yaratish
python manage.py migrate
```

### 3. Superuser Yaratish

```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: (o'zingizniki)
```

### 4. Development Server

```bash
python manage.py runserver
```

Server ishga tushadi: **http://localhost:8000**

### 5. Browser da Ochish

1. **Frontend:** http://localhost:8000/
   - Portfolio dizayni to'liq ishlab turadi
   - Barcha CSS, JS, rasmlar Django static files orqali yuklanadi

2. **Admin Panel:** http://localhost:8000/admin/
   - Superuser bilan kiring
   - Ma'lumot qo'shing: Profile, Services, Projects, Blog va hokazo

3. **API:** http://localhost:8000/api/
   - JSON formatda ma'lumotlar

## Ma'lumot Qo'shish (Admin orqali)

### 1. Profile Yaratish
1. Admin panelga kiring
2. **Profile** → **Add Profile**
3. To'ldiring:
   - Name: Ismingiz
   - Title: Kasbingiz (masalan: "Full Stack Developer")
   - Avatar: Rasm yuklang
   - Bio: O'zingiz haqingizda
   - Email, Phone, Birthday, Location
   - Social media links

### 2. Services Qo'shish
**Portfolio → Services → Add Service**
- Name: "Web Development"
- Description: Xizmat tavsifi
- Icon: Rasm yuklash (optional)
- Order: 1 (tartib raqami)

### 3. Timeline (Ta'lim/Tajriba)
**Portfolio → Timeline Entries → Add**
- Type: Education yoki Experience
- Title: "University of California"
- Institution: "Berkeley"
- Start Date / End Date
- Description

### 4. Skills
**Portfolio → Skills → Add**
- Name: "Python"
- Proficiency: 90 (0-100)
- Order: 1

### 5. Projects
**Portfolio → Projects → Add**
- Title: "E-commerce Website"
- Description: Loyiha tavsifi
- Image: Loyiha rasmi
- Category: Kategoriya tanlang (oldin yaratish kerak)
- Link: Demo link
- GitHub URL
- Technologies: "Django, React, PostgreSQL"

### 6. Blog Posts
**Portfolio → Blog Posts → Add**
- Title: "My First Blog Post"
- Slug: auto-generated
- Content: Blog mazmuni
- Excerpt: Qisqa tavsif
- Featured Image
- Category: "Technology"
- Published Date

## Static Files Ishlashi

Django `{% static %}` tags ishlatadi:

```django
{% load static %}

<!-- CSS -->
<link rel="stylesheet" href="{% static 'portfolio/css/style.css' %}">

<!-- JavaScript -->
<script src="{% static 'portfolio/js/script.js' %}"></script>

<!-- Images -->
<img src="{% static 'portfolio/images/my-avatar.png' %}" alt="Avatar">
```

## API bilan Ishlash (JavaScript)

Frontend da API dan ma'lumot olish:

```javascript
// Profil olish
fetch('http://localhost:8000/api/profile/')
  .then(res => res.json())
  .then(data => console.log(data));

// Loyihalarni olish
fetch('http://localhost:8000/api/projects/')
  .then(res => res.json())
  .then(projects => console.log(projects));

// Kontakt forma yuborish
fetch('http://localhost:8000/api/contact/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    full_name: 'John Doe',
    email: 'john@example.com',
    message: 'Hello!'
  })
});
```

## Development Tips

### Static Files Collect (Production uchun)

```bash
python manage.py collectstatic
```

### Database Reset

```bash
# Database o'chirish
rm db.sqlite3

# Qayta yaratish
python manage.py migrate
python manage.py createsuperuser
```

### Django Shell (Testing)

```bash
python manage.py shell

>>> from portfolio.models import Profile
>>> profile = Profile.objects.create(
...     name='Test User',
...     title='Developer',
...     email='test@example.com'
... )
```

## Production Deployment

### 1. Settings yangilash

`backend/config/settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'strong_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static & Media files
STATIC_ROOT = '/var/www/portfolio/static/'
MEDIA_ROOT = '/var/www/portfolio/media/'
```

### 2. Environment Variables

`.env` fayl yaratish:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

### 3. Gunicorn + Nginx

```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Muammolarni Hal Qilish

### Static files yuklanmayapti?

```bash
python manage.py collectstatic --clear
```

### Admin panelda CSS yo'q?

```bash
python manage.py collectstatic
```

### API CORS xatolari?

`settings.py` da:
```python
CORS_ALLOW_ALL_ORIGINS = True  # Development
```

## Foydali Commandlar

```bash
# Migratsiyalarni ko'rish
python manage.py showmigrations

# Server loglarni ko'rish
python manage.py runserver --verbosity 2

# Database shell
python manage.py dbshell

# Test ishga tushirish
python manage.py test
```

## Keyingi Qadamlar

1. ✅ Backend tayyor va ishlamoqda
2. ✅ Frontend Django template sifatida integratsiya qilindi
3. ✅ Static files to'g'ri sozlandi
4. 🔄 Admin orqali ma'lumot qo'shing
5. 🔄 API testing qiling
6. 🔄 Production ga deploy qiling

## Yordam

Savollar bo'lsa:
- Backend README: `backend/README.md`
- Integration Guide: `INTEGRATION_GUIDE.md`
- API Reference: `API_QUICK_REFERENCE.md`

Muammolar uchun:
- Django logs: `python manage.py runserver --verbosity 2`
- Browser console: F12 → Console
- Network tab: Static files yuklanishini tekshiring

---

**Muvaffaqiyatlar!** 🎉

Portfolio backend va frontend to'liq tayyor va ishlamoqda!
