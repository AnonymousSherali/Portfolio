from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet, ServiceViewSet, TimelineViewSet, SkillViewSet,
    ProjectCategoryViewSet, ProjectViewSet, TestimonialViewSet,
    ClientViewSet, BlogPostViewSet, ContactMessageCreateView
)

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'timeline', TimelineViewSet, basename='timeline')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'categories', ProjectCategoryViewSet, basename='category')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'blog', BlogPostViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactMessageCreateView.as_view(), name='contact'),
]
