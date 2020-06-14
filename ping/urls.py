from django.urls import path
from .views import ping_response
urlpatterns = [
    path('ping', ping_response)
]
