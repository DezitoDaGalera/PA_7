from .views import endereco_list_APIview
from django.urls import path

urlpatterns = [
    path('enderecos/', endereco_list_APIview)
]
