"""
Simple healthcheck view for Railway deployment monitoring.
"""
from django.http import JsonResponse
from django.views import View


class HealthCheckView(View):
    """
    Healthcheck endpoint for Railway.
    Returns 200 OK with basic service status.
    """
    def get(self, request):
        return JsonResponse({
            'status': 'healthy',
            'service': 'portfolio',
            'message': 'Service is running'
        }, status=200)
