from django.contrib import admin
from .models import (
    Profile, Service, TimelineEntry, Skill,
    ProjectCategory, Project, Testimonial, Client,
    BlogPost, ContactMessage
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone', 'location']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'avatar', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'birthday', 'location')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'github_url')
        }),
    )

    def has_add_permission(self, request):
        # Prevent creating multiple profiles
        return not Profile.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'institution', 'start_date', 'end_date', 'is_current', 'order', 'is_active']
    list_filter = ['type', 'is_active']
    search_fields = ['title', 'institution', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['-start_date', 'order']
    date_hierarchy = 'start_date'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'category']
    list_editable = ['proficiency', 'order', 'is_active']
    ordering = ['order', 'name']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_date', 'featured', 'order', 'is_active']
    list_filter = ['category', 'featured', 'is_active', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order', 'is_active']
    ordering = ['-featured', 'order', '-created_date']
    date_hierarchy = 'created_date'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image', 'category')
        }),
        ('Links', {
            'fields': ('link', 'github_url')
        }),
        ('Details', {
            'fields': ('technologies', 'created_date', 'featured', 'order', 'is_active')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'date', 'order', 'is_active']
    list_filter = ['is_active', 'date']
    search_fields = ['client_name', 'content']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-date']
    date_hierarchy = 'date'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_date', 'featured', 'is_published', 'view_count']
    list_filter = ['category', 'featured', 'is_published', 'published_date']
    search_fields = ['title', 'content', 'excerpt']
    list_editable = ['featured', 'is_published']
    ordering = ['-published_date']
    date_hierarchy = 'published_date'
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('published_date', 'featured', 'is_published')
        }),
        ('Statistics', {
            'fields': ('view_count',),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'submitted_date', 'is_read']
    list_filter = ['is_read', 'submitted_date']
    search_fields = ['full_name', 'email', 'message']
    list_editable = ['is_read']
    ordering = ['-submitted_date']
    date_hierarchy = 'submitted_date'
    readonly_fields = ['full_name', 'email', 'message', 'submitted_date']

    def has_add_permission(self, request):
        # Contact messages should only come from the API
        return False


# Customize admin site header
admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin Portal'
admin.site.index_title = 'Welcome to Portfolio Administration'
