from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import (
    Profile, Service, TimelineEntry, Skill,
    ProjectCategory, Project, Testimonial, Client,
    BlogPost, ContactMessage
)
from .serializers import (
    ProfileSerializer, ServiceSerializer, TimelineEntrySerializer,
    SkillSerializer, ProjectCategorySerializer, ProjectSerializer,
    TestimonialSerializer, ClientSerializer, BlogPostListSerializer,
    BlogPostDetailSerializer, ContactMessageSerializer
)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for portfolio profile.
    GET /api/profile/ - Get profile information
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        # Return the first (and should be only) profile
        profile = self.queryset.first()
        if profile:
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for services.
    GET /api/services/ - List all active services
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class TimelineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for timeline entries (education & experience).
    GET /api/timeline/ - List all timeline entries
    GET /api/timeline/?type=education - Filter by type
    GET /api/timeline/?type=experience - Filter by type
    """
    queryset = TimelineEntry.objects.filter(is_active=True)
    serializer_class = TimelineEntrySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        entry_type = self.request.query_params.get('type', None)
        if entry_type in ['education', 'experience']:
            queryset = queryset.filter(type=entry_type)
        return queryset


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for skills.
    GET /api/skills/ - List all active skills
    """
    queryset = Skill.objects.filter(is_active=True)
    serializer_class = SkillSerializer


class ProjectCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for project categories.
    GET /api/categories/ - List all categories
    """
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for projects.
    GET /api/projects/ - List all active projects
    GET /api/projects/?category=web-design - Filter by category slug
    GET /api/projects/?featured=true - Get featured projects only
    GET /api/projects/{id}/ - Get project detail
    """
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by category
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Filter by featured
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = queryset.filter(featured=True)

        return queryset


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for testimonials.
    GET /api/testimonials/ - List all active testimonials
    """
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer


class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for clients.
    GET /api/clients/ - List all active clients
    """
    queryset = Client.objects.filter(is_active=True)
    serializer_class = ClientSerializer


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for blog posts.
    GET /api/blog/ - List all published blog posts (paginated)
    GET /api/blog/{slug}/ - Get blog post detail
    GET /api/blog/?featured=true - Get featured posts only
    """
    queryset = BlogPost.objects.filter(is_published=True)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return BlogPostListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by featured
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = queryset.filter(featured=True)

        # Filter by category
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__icontains=category)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        # Increment view count when blog post is viewed
        instance = self.get_object()
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ContactMessageCreateView(generics.CreateAPIView):
    """
    API endpoint for contact form submissions.
    POST /api/contact/ - Submit a contact message
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Thank you! Your message has been sent successfully."},
            status=status.HTTP_201_CREATED
        )


class PortfolioHomeView(TemplateView):
    """
    Frontend portfolio template view.
    Renders the main portfolio HTML page with Django static files.
    """
    template_name = 'portfolio/index.html'
