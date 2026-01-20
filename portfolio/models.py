from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    """Portfolio owner's profile information"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthday = models.DateField()
    location = models.CharField(max_length=200)

    # Social media links
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name


class Service(models.Model):
    """Services offered by the portfolio owner"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class TimelineEntry(models.Model):
    """Education and work experience timeline"""
    TYPE_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Experience'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, help_text='School or Company name')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text='Leave empty for current position')
    description = models.TextField()
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = 'Timeline Entry'
        verbose_name_plural = 'Timeline Entries'

    def __str__(self):
        return f"{self.title} at {self.institution}"

    @property
    def is_current(self):
        return self.end_date is None


class Skill(models.Model):
    """Skills with proficiency levels"""
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        default=50,
        help_text='Proficiency percentage (0-100)'
    )
    category = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class ProjectCategory(models.Model):
    """Categories for portfolio projects"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )
    link = models.URLField(blank=True, help_text='Project live URL')
    github_url = models.URLField(blank=True, help_text='GitHub repository URL')
    technologies = models.CharField(max_length=500, help_text='Comma-separated technologies used')
    created_date = models.DateField()
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_date']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100)
    client_avatar = models.ImageField(upload_to='testimonials/')
    content = models.TextField()
    date = models.DateField()
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Testimonial from {self.client_name}"


class Client(models.Model):
    """Client logos"""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')
    website = models.URLField(blank=True)
    order = models.IntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(help_text='Short preview text')
    featured_image = models.ImageField(upload_to='blog/')
    category = models.CharField(max_length=100, default='Design')
    published_date = models.DateField()
    updated_date = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    """Contact form submissions"""
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_date']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.full_name} - {self.submitted_date.strftime('%Y-%m-%d')}"
