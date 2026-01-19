# API Quick Reference

Portfolio Backend API ning tez ma'lumotnomasi.

## Base URL
```
http://localhost:8000/api
```

## Endpoints

### 📋 Profile
```bash
GET /api/profile/
```
**Response:**
```json
{
  "id": 1,
  "name": "Richard Hanrick",
  "title": "Web Developer",
  "avatar": "/media/profile/avatar.jpg",
  "bio": "I'm Creative Director and UI/UX Designer...",
  "email": "richard@example.com",
  "phone": "+1 (213) 352-2795",
  "birthday": "1982-06-23",
  "location": "Sacramento, California, USA",
  "facebook_url": "https://facebook.com/...",
  "twitter_url": "https://twitter.com/...",
  "instagram_url": "https://instagram.com/..."
}
```

---

### 🛠️ Services
```bash
GET /api/services/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Web Design",
    "description": "The most modern and high-quality design...",
    "icon": "/media/services/icon-design.svg",
    "order": 1,
    "is_active": true
  }
]
```

---

### 📚 Timeline (Education & Experience)
```bash
GET /api/timeline/
GET /api/timeline/?type=education
GET /api/timeline/?type=experience
```
**Response:**
```json
[
  {
    "id": 1,
    "type": "education",
    "title": "University of California",
    "institution": "Berkeley",
    "start_date": "2007-09-01",
    "end_date": "2011-05-30",
    "description": "Bachelor's degree in Computer Science",
    "is_current": false,
    "order": 1
  }
]
```

---

### 💪 Skills
```bash
GET /api/skills/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Web Design",
    "proficiency": 80,
    "category": "Design",
    "order": 1,
    "is_active": true
  }
]
```

---

### 📁 Project Categories
```bash
GET /api/categories/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Web Design",
    "slug": "web-design",
    "description": "Beautiful and responsive web designs",
    "projects_count": 5
  }
]
```

---

### 🎨 Projects
```bash
GET /api/projects/
GET /api/projects/?category=web-design
GET /api/projects/?featured=true
GET /api/projects/1/
```
**Response (List):**
```json
[
  {
    "id": 1,
    "title": "Finance Dashboard",
    "description": "Modern finance tracking application",
    "image": "/media/projects/project-1.jpg",
    "category": 1,
    "category_name": "Web Design",
    "link": "https://example.com",
    "github_url": "https://github.com/...",
    "technologies": "React, TypeScript, Tailwind CSS",
    "technologies_list": ["React", "TypeScript", "Tailwind CSS"],
    "created_date": "2023-10-15",
    "featured": true,
    "order": 1
  }
]
```

---

### 💬 Testimonials
```bash
GET /api/testimonials/
```
**Response:**
```json
[
  {
    "id": 1,
    "client_name": "John Doe",
    "client_avatar": "/media/testimonials/client-1.jpg",
    "content": "Richard was hired to create...",
    "date": "2023-09-15",
    "order": 1,
    "is_active": true
  }
]
```

---

### 🏢 Clients
```bash
GET /api/clients/
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Google",
    "logo": "/media/clients/google.png",
    "website": "https://google.com",
    "order": 1,
    "is_active": true
  }
]
```

---

### 📝 Blog Posts
```bash
GET /api/blog/
GET /api/blog/?page=2
GET /api/blog/?featured=true
GET /api/blog/my-first-blog-post/
```
**Response (List - Paginated):**
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/blog/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Design Trends in 2024",
      "slug": "design-trends-2024",
      "excerpt": "Exploring the latest design trends...",
      "featured_image": "/media/blog/blog-1.jpg",
      "category": "Design",
      "published_date": "2024-01-15",
      "view_count": 125,
      "featured": true
    }
  ]
}
```

**Response (Detail):**
```json
{
  "id": 1,
  "title": "Design Trends in 2024",
  "slug": "design-trends-2024",
  "content": "Full blog post content here...",
  "excerpt": "Exploring the latest design trends...",
  "featured_image": "/media/blog/blog-1.jpg",
  "category": "Design",
  "published_date": "2024-01-15",
  "updated_date": "2024-01-16",
  "featured": true,
  "is_published": true,
  "view_count": 126
}
```

---

### 📧 Contact Form
```bash
POST /api/contact/
```
**Request Body:**
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, I would like to work with you!"
}
```
**Response:**
```json
{
  "message": "Thank you! Your message has been sent successfully."
}
```

---

## JavaScript Examples

### Fetch Profile
```javascript
fetch('http://localhost:8000/api/profile/')
  .then(res => res.json())
  .then(data => console.log(data));
```

### Fetch Projects with Filter
```javascript
fetch('http://localhost:8000/api/projects/?category=web-design')
  .then(res => res.json())
  .then(projects => console.log(projects));
```

### Submit Contact Form
```javascript
fetch('http://localhost:8000/api/contact/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    full_name: 'John Doe',
    email: 'john@example.com',
    message: 'Hello!'
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

### Async/Await Example
```javascript
async function loadPortfolio() {
  try {
    const profile = await fetch('/api/profile/').then(r => r.json());
    const projects = await fetch('/api/projects/').then(r => r.json());
    console.log(profile, projects);
  } catch (error) {
    console.error('Error:', error);
  }
}
```

---

## Common Filters

| Endpoint | Filter | Example |
|----------|--------|---------|
| Timeline | `type` | `/api/timeline/?type=education` |
| Projects | `category` | `/api/projects/?category=web-design` |
| Projects | `featured` | `/api/projects/?featured=true` |
| Blog | `page` | `/api/blog/?page=2` |
| Blog | `featured` | `/api/blog/?featured=true` |

---

## Error Responses

**404 Not Found:**
```json
{
  "detail": "Not found."
}
```

**400 Bad Request:**
```json
{
  "field_name": ["This field is required."]
}
```

**500 Server Error:**
```json
{
  "detail": "Internal server error."
}
```

---

## Testing with cURL

### Get Profile
```bash
curl http://localhost:8000/api/profile/
```

### Get Projects
```bash
curl http://localhost:8000/api/projects/
```

### Submit Contact Form
```bash
curl -X POST http://localhost:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"full_name":"John Doe","email":"john@example.com","message":"Hello!"}'
```

---

## Admin Panel

**URL:** `http://localhost:8000/admin/`

Login with superuser credentials to manage all content.

**Available Sections:**
- Profile
- Services
- Timeline Entries
- Skills
- Project Categories
- Projects
- Testimonials
- Clients
- Blog Posts
- Contact Messages

---

## Tips

1. **CORS**: Make sure `CORS_ALLOW_ALL_ORIGINS = True` in development
2. **Media Files**: Uploaded files are served at `/media/`
3. **Pagination**: Blog posts are paginated (10 per page by default)
4. **View Count**: Blog post views auto-increment on detail view
5. **Ordering**: Most models support `order` field for custom sorting

---

## Support

For issues: Check backend logs with `python manage.py runserver --verbosity 2`
