"""
URL configuration for the portfolio project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]

# Static files are served by WhiteNoise in production and by the staticfiles
# app in development, so only user uploads need an explicit route. Django's
# static() helper is a no-op when DEBUG is False, hence the serve() view: it
# keeps admin-uploaded images working on Railway without an external CDN.
urlpatterns += [
    re_path(
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]
