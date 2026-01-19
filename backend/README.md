# Portfolio Backend API

Django REST API backend for a portfolio website.

## Features

- **Profile Management**: Personal information, contact details, and social media links
- **Services**: Display offered services and skills
- **Timeline**: Education and work experience
- **Skills**: Technical skills with proficiency levels
- **Projects**: Portfolio projects with categories and filtering
- **Testimonials**: Client reviews and testimonials
- **Clients**: Client logos showcase
- **Blog**: Blog posts with categories and view tracking
- **Contact**: Contact form submissions
- **Admin Panel**: Full Django admin interface for content management

## Tech Stack

- Django 5.0
- Django REST Framework 3.14
- SQLite (development) - Can be changed to PostgreSQL/MySQL for production
- Pillow for image handling
- CORS headers for frontend integration

## API Endpoints

### Public Endpoints

```
GET  /api/profile/              - Get profile information
GET  /api/services/             - List all services
GET  /api/timeline/             - List education & experience
GET  /api/timeline/?type=education   - Filter timeline by type
GET  /api/skills/               - List all skills
GET  /api/categories/           - List project categories
GET  /api/projects/             - List all projects
GET  /api/projects/?category=web-design  - Filter projects by category
GET  /api/projects/{id}/        - Get project detail
GET  /api/testimonials/         - List testimonials
GET  /api/clients/              - List clients
GET  /api/blog/                 - List blog posts (paginated)
GET  /api/blog/{slug}/          - Get blog post detail
POST /api/contact/              - Submit contact message
```

### Admin Panel

```
/admin/  - Django admin interface
```

## Installation & Setup

### 1. Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### 2. Create Virtual Environment

```bash
cd backend
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000/api/`
Admin panel at: `http://localhost:8000/admin/`

## Project Structure

```
backend/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── portfolio/             # Main app
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URLs
│   └── admin.py           # Admin configuration
├── media/                 # Uploaded files (created automatically)
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Models Overview

1. **Profile** - Portfolio owner information
2. **Service** - Services offered
3. **TimelineEntry** - Education and experience
4. **Skill** - Technical skills with proficiency
5. **ProjectCategory** - Project categories
6. **Project** - Portfolio projects
7. **Testimonial** - Client testimonials
8. **Client** - Client logos
9. **BlogPost** - Blog articles
10. **ContactMessage** - Contact form submissions

## Admin Panel Features

- Full CRUD operations for all models
- Image upload support
- Rich text editing for blog posts
- Filter and search capabilities
- Order management for display sequences
- Active/inactive toggles
- View statistics for blog posts
- Contact message management

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### CORS Configuration

Update `config/settings.py` to add your frontend URLs:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    # Add your frontend URLs here
]
```

### Database Configuration

For production, update `DATABASES` in `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Usage Examples

### Adding Content via Admin

1. Go to `http://localhost:8000/admin/`
2. Login with superuser credentials
3. Add/edit content for each section
4. Upload images for projects, blog posts, etc.

### Fetching Data from Frontend

```javascript
// Fetch profile
fetch('http://localhost:8000/api/profile/')
  .then(res => res.json())
  .then(data => console.log(data));

// Fetch projects
fetch('http://localhost:8000/api/projects/')
  .then(res => res.json())
  .then(data => console.log(data));

// Submit contact form
fetch('http://localhost:8000/api/contact/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    full_name: 'John Doe',
    email: 'john@example.com',
    message: 'Hello!'
  })
});
```

## Development

### Creating Migrations

After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests

```bash
python manage.py test
```

### Collecting Static Files

For production:

```bash
python manage.py collectstatic
```

## Production Deployment

1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static/media file serving (AWS S3, Cloudinary, etc.)
4. Configure allowed hosts
5. Use environment variables for sensitive data
6. Set up HTTPS
7. Use production-grade server (Gunicorn + Nginx)

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue in the GitHub repository.
