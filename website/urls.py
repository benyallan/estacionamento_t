from django.urls import path, include
from .views import home, contato

urlpatterns = [
    path('', home, name='website_home'),
    path('contato', contato, name='website_contato'),
]
