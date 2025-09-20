from django.urls import path
from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.home_page, name='home'),
    # path('policies/', views.policies_page, name='policies'),
    # path('', views.home_view, name='home'),
    # path('gallery/', views.gallery_view, name='gallery'),
]
