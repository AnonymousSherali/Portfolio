from rest_framework import serializers
from .models import (
    Profile, Service, TimelineEntry, Skill,
    ProjectCategory, Project, Testimonial, Client,
    BlogPost, ContactMessage
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TimelineEntrySerializer(serializers.ModelSerializer):
    is_current = serializers.ReadOnlyField()

    class Meta:
        model = TimelineEntry
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectCategorySerializer(serializers.ModelSerializer):
    projects_count = serializers.SerializerMethodField()

    class Meta:
        model = ProjectCategory
        fields = ['id', 'name', 'slug', 'description', 'projects_count']

    def get_projects_count(self, obj):
        return obj.projects.filter(is_active=True).count()


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    technologies_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_technologies_list(self, obj):
        if obj.technologies:
            return [tech.strip() for tech in obj.technologies.split(',')]
        return []


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BlogPostListSerializer(serializers.ModelSerializer):
    """Serializer for blog post list view"""
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'category', 'published_date', 'view_count', 'featured'
        ]


class BlogPostDetailSerializer(serializers.ModelSerializer):
    """Serializer for blog post detail view"""
    class Meta:
        model = BlogPost
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'full_name', 'email', 'message', 'submitted_date']
        read_only_fields = ['submitted_date']
