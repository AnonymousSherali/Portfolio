"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import PortfolioHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PortfolioHomeView.as_view(), name='home'),  # Frontend homepage
    path('', include('portfolio.urls')),  # Portfolio app URLs (API and templates)
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
