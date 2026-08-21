"""Smoke tests covering the pages and API endpoints the site depends on."""

from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import (
    BlogPost, Client as ClientLogo, ContactMessage, Profile,
    Project, ProjectCategory, Service, Skill, Testimonial, TimelineEntry,
)


class PageRenderTests(TestCase):
    """The homepage must render both with an empty database and with content."""

    def test_homepage_renders_without_any_data(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_renders_with_content(self):
        Profile.objects.create(
            name='Sherali Toshniyozov', title='Web developer', bio='Hello',
            email='me@example.com', phone='+998900000000',
            birthday=date(2000, 1, 1), location='Tashkent',
        )
        Service.objects.create(name='Web development', description='Sites')
        Skill.objects.create(name='Django', proficiency=90)
        TimelineEntry.objects.create(
            type='education', title='CS', institution='University',
            start_date=date(2018, 9, 1), description='Studied CS',
        )
        category = ProjectCategory.objects.create(name='Web development')
        Project.objects.create(
            title='Portfolio', description='This site', category=category,
            technologies='Django', created_date=date(2024, 1, 1),
        )
        Testimonial.objects.create(
            client_name='Ali', content='Great work', date=date(2024, 1, 1),
        )
        ClientLogo.objects.create(name='Acme')
        BlogPost.objects.create(
            title='First post', content='Body', excerpt='Preview',
            published_date=date(2024, 1, 1),
        )

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sherali Toshniyozov')
        self.assertContains(response, 'University')  # timeline institution
        self.assertContains(response, 'First post')

    def test_healthcheck_returns_ok(self):
        response = self.client.get(reverse('healthcheck'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'healthy')


class BlogDetailTests(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(
            title='Design digest', content='Body text', excerpt='Preview',
            published_date=date(2024, 1, 1),
        )

    def test_slug_is_generated(self):
        self.assertEqual(self.post.slug, 'design-digest')

    def test_duplicate_titles_get_unique_slugs(self):
        second = BlogPost.objects.create(
            title='Design digest', content='Other', excerpt='Preview',
            published_date=date(2024, 2, 1),
        )
        self.assertEqual(second.slug, 'design-digest-2')

    def test_detail_page_renders_and_counts_view(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Design digest')
        self.post.refresh_from_db()
        self.assertEqual(self.post.view_count, 1)

    def test_unpublished_post_is_hidden(self):
        self.post.is_published = False
        self.post.save()
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 404)


class ContactApiTests(TestCase):
    def test_form_submission_creates_message(self):
        response = self.client.post(reverse('contact'), {
            'full_name': 'Ali Valiyev',
            'email': 'ali@example.com',
            'message': 'Salom!',
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(ContactMessage.objects.filter(email='ali@example.com').exists())

    def test_invalid_email_is_rejected(self):
        response = self.client.post(reverse('contact'), {
            'full_name': 'Ali', 'email': 'not-an-email', 'message': 'Salom',
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)


class ApiEndpointTests(TestCase):
    """These 404'd before the duplicate '' route in config/urls.py was removed."""

    def test_api_endpoints_are_reachable(self):
        for name in ['service', 'skill', 'project', 'testimonial', 'client', 'blog']:
            with self.subTest(endpoint=name):
                response = self.client.get(reverse(f'{name}-list'))
                self.assertEqual(response.status_code, 200)
