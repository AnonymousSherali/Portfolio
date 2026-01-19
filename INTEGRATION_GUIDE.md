# Frontend-Backend Integration Guide

Bu qo'llanma sizning mavjud frontend (HTML/CSS/JS) va yangi Django backend ni qanday bog'lashni ko'rsatadi.

## Tezkor Boshlash (Quick Start)

### 1. Backend ni ishga tushirish

```bash
cd backend

# Virtual environment yaratish
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki Windows da: venv\Scripts\activate

# Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# Database migratsiyalari
python manage.py makemigrations
python manage.py migrate

# Admin user yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver
```

Backend `http://localhost:8000` da ishga tushadi.

### 2. Admin panel orqali ma'lumot qo'shish

1. Brauzerda ochish: `http://localhost:8000/admin/`
2. Superuser login va parol bilan kirish
3. Har bir bo'limga ma'lumot qo'shish:
   - Profile (O'zingiz haqingizda)
   - Services (Xizmatlar)
   - Timeline (Ta'lim va tajriba)
   - Skills (Ko'nikmalar)
   - Projects (Loyihalar)
   - Testimonials (Mijozlar sharhlari)
   - Clients (Mijozlar logotiplari)
   - Blog Posts (Blog postlar)

### 3. Frontend ni yangilash

Mavjud `index.html` faylingizni API dan ma'lumot olish uchun yangilash kerak.

## API Endpoints

| Endpoint | Metod | Tavsif |
|----------|-------|--------|
| `/api/profile/` | GET | Profil ma'lumotlari |
| `/api/services/` | GET | Xizmatlar ro'yxati |
| `/api/timeline/` | GET | Ta'lim va tajriba |
| `/api/skills/` | GET | Ko'nikmalar |
| `/api/projects/` | GET | Loyihalar ro'yxati |
| `/api/projects/?category=web-design` | GET | Kategoriya bo'yicha filter |
| `/api/testimonials/` | GET | Sharhlar |
| `/api/clients/` | GET | Mijozlar |
| `/api/blog/` | GET | Blog postlar |
| `/api/blog/{slug}/` | GET | Bitta blog post |
| `/api/contact/` | POST | Kontakt forma yuborish |

## Frontend Integratsiya Misollari

### 1. API dan ma'lumot olish (Fetch Profile)

`assets/js/api.js` fayl yarating:

```javascript
// API Base URL
const API_BASE_URL = 'http://localhost:8000/api';

// Profil ma'lumotlarini olish
async function fetchProfile() {
  try {
    const response = await fetch(`${API_BASE_URL}/profile/`);
    const data = await response.json();
    updateProfileUI(data);
  } catch (error) {
    console.error('Error fetching profile:', error);
  }
}

function updateProfileUI(profile) {
  // Sidebar dagi ma'lumotlarni yangilash
  document.querySelector('.info-content .name').textContent = profile.name;
  document.querySelector('.info-content .title').textContent = profile.title;

  // Avatar
  if (profile.avatar) {
    document.querySelector('.avatar-box img').src = profile.avatar;
  }

  // Contact info
  document.querySelector('.contact-info .email').href = `mailto:${profile.email}`;
  document.querySelector('.contact-info .email').textContent = profile.email;
  document.querySelector('.contact-info .phone').textContent = profile.phone;
  document.querySelector('.contact-info .location').textContent = profile.location;

  // Bio
  document.querySelector('.about-text p').textContent = profile.bio;
}
```

### 2. Xizmatlarni yuklash (Load Services)

```javascript
async function fetchServices() {
  try {
    const response = await fetch(`${API_BASE_URL}/services/`);
    const services = await response.json();
    renderServices(services);
  } catch (error) {
    console.error('Error fetching services:', error);
  }
}

function renderServices(services) {
  const container = document.querySelector('.service-list');
  container.innerHTML = ''; // Tozalash

  services.forEach(service => {
    const serviceItem = `
      <li class="service-item">
        <div class="service-icon-box">
          <img src="${service.icon || './assets/images/icon-design.svg'}" alt="${service.name} icon" width="40">
        </div>
        <div class="service-content-box">
          <h4 class="h4 service-item-title">${service.name}</h4>
          <p class="service-item-text">${service.description}</p>
        </div>
      </li>
    `;
    container.innerHTML += serviceItem;
  });
}
```

### 3. Loyihalarni yuklash va filterlash (Load & Filter Projects)

```javascript
let allProjects = [];

async function fetchProjects() {
  try {
    const response = await fetch(`${API_BASE_URL}/projects/`);
    allProjects = await response.json();
    renderProjects(allProjects);
  } catch (error) {
    console.error('Error fetching projects:', error);
  }
}

function renderProjects(projects) {
  const container = document.querySelector('.project-list');
  container.innerHTML = '';

  projects.forEach(project => {
    const projectItem = `
      <li class="project-item active" data-filter-item data-category="${project.category_name}">
        <a href="${project.link || '#'}">
          <figure class="project-img">
            <div class="project-item-icon-box">
              <ion-icon name="eye-outline"></ion-icon>
            </div>
            <img src="${project.image}" alt="${project.title}" loading="lazy">
          </figure>
          <h3 class="project-title">${project.title}</h3>
          <p class="project-category">${project.category_name}</p>
        </a>
      </li>
    `;
    container.innerHTML += projectItem;
  });
}

// Filter funksiyasi
function filterProjects(category) {
  if (category === 'all') {
    renderProjects(allProjects);
  } else {
    const filtered = allProjects.filter(p =>
      p.category_name.toLowerCase() === category.toLowerCase()
    );
    renderProjects(filtered);
  }
}

// Filter tugmalariga event listener
document.querySelectorAll('[data-filter-btn]').forEach(btn => {
  btn.addEventListener('click', function() {
    const category = this.dataset.filterBtn;
    filterProjects(category);
  });
});
```

### 4. Blog postlarni yuklash (Load Blog Posts)

```javascript
async function fetchBlogPosts() {
  try {
    const response = await fetch(`${API_BASE_URL}/blog/`);
    const data = await response.json();
    renderBlogPosts(data.results); // Paginated response
  } catch (error) {
    console.error('Error fetching blog posts:', error);
  }
}

function renderBlogPosts(posts) {
  const container = document.querySelector('.blog-posts-list');
  container.innerHTML = '';

  posts.forEach(post => {
    const blogItem = `
      <li class="blog-post-item">
        <a href="blog-detail.html?slug=${post.slug}">
          <figure class="blog-banner-box">
            <img src="${post.featured_image}" alt="${post.title}" loading="lazy">
          </figure>
          <div class="blog-content">
            <div class="blog-meta">
              <p class="blog-category">${post.category}</p>
              <span class="dot"></span>
              <time datetime="${post.published_date}">${formatDate(post.published_date)}</time>
            </div>
            <h3 class="h3 blog-item-title">${post.title}</h3>
            <p class="blog-text">${post.excerpt}</p>
          </div>
        </a>
      </li>
    `;
    container.innerHTML += blogItem;
  });
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('en-US', options);
}
```

### 5. Kontakt forma yuborish (Submit Contact Form)

```javascript
async function submitContactForm(formData) {
  try {
    const response = await fetch(`${API_BASE_URL}/contact/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        full_name: formData.fullName,
        email: formData.email,
        message: formData.message
      })
    });

    const data = await response.json();

    if (response.ok) {
      alert('Message sent successfully!');
      // Formani tozalash
      document.querySelector('form[data-form]').reset();
    } else {
      alert('Error sending message. Please try again.');
    }
  } catch (error) {
    console.error('Error submitting form:', error);
    alert('Network error. Please try again.');
  }
}

// Form submit event
const form = document.querySelector('form[data-form]');
form.addEventListener('submit', function(e) {
  e.preventDefault();

  const formData = {
    fullName: this.querySelector('[name="fullname"]').value,
    email: this.querySelector('[name="email"]').value,
    message: this.querySelector('[name="message"]').value
  };

  submitContactForm(formData);
});
```

### 6. Timeline (Ta'lim va Tajriba) yuklash

```javascript
async function fetchTimeline() {
  try {
    // Education
    const eduResponse = await fetch(`${API_BASE_URL}/timeline/?type=education`);
    const education = await eduResponse.json();
    renderTimeline(education, 'education');

    // Experience
    const expResponse = await fetch(`${API_BASE_URL}/timeline/?type=experience`);
    const experience = await expResponse.json();
    renderTimeline(experience, 'experience');
  } catch (error) {
    console.error('Error fetching timeline:', error);
  }
}

function renderTimeline(items, type) {
  const container = document.querySelector(`.timeline-list.${type}`);
  container.innerHTML = '';

  items.forEach(item => {
    const timelineItem = `
      <li class="timeline-item">
        <h4 class="h4 timeline-item-title">${item.title}</h4>
        <span>${item.start_date} — ${item.end_date || 'Present'}</span>
        <p class="timeline-text">${item.description}</p>
      </li>
    `;
    container.innerHTML += timelineItem;
  });
}
```

## HTML ga qo'shish kerak

`index.html` ga API script ni qo'shing:

```html
<!-- Oxirida, script.js dan oldin -->
<script src="./assets/js/api.js"></script>
<script>
  // Sahifa yuklanganda ma'lumotlarni olish
  document.addEventListener('DOMContentLoaded', function() {
    fetchProfile();
    fetchServices();
    fetchProjects();
    fetchTimeline();
    fetchBlogPosts();
  });
</script>
```

## CORS Muammolarini hal qilish

Agar CORS xatosi ko'rsangiz:

1. Backend `config/settings.py` da `CORS_ALLOW_ALL_ORIGINS = True` borligini tekshiring
2. Yoki o'z frontend URL ni qo'shing:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",  # Live Server
    "http://127.0.0.1:5500",
    "http://localhost:3000",
]
```

## Media Fayllar

Backend media fayllarni `http://localhost:8000/media/` da beradi.

Masalan:
- Avatar: `http://localhost:8000/media/profile/avatar.jpg`
- Project image: `http://localhost:8000/media/projects/project1.jpg`

## Production uchun

Production da API URL ni o'zgartiring:

```javascript
const API_BASE_URL = 'https://your-domain.com/api';
```

## Qo'shimcha Maslahatlar

1. **Loading State**: Ma'lumotlar yuklanayotganda loading spinner ko'rsating
2. **Error Handling**: Xatoliklarni to'g'ri handle qiling
3. **Caching**: Tez-tez o'zgarmaydigan ma'lumotlarni cache qiling
4. **Optimizatsiya**: Rasmlarni lazy loading bilan yuklang
5. **SEO**: Server-side rendering yoki pre-rendering ishlatish mumkin

## Yordam

Savollar bo'lsa, GitHub Issues da murojaat qiling.
