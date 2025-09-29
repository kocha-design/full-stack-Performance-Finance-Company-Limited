from django.urls import path
from . import views

urlpatterns = [
    path('policies/', views.policies, name='policies'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-of-use/', views.terms_of_use, name='terms-of-use'),
    path('cookies-policy/', views.cookies_policy, name='cookies-policy'),
    path('data-rights/', views.data_rights, name='data-rights'),
    path('security/', views.security, name='security'),
]
