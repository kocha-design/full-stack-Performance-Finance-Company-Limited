from django.urls import path
from . import views

app_name = 'policies'

urlpatterns = [
    
    path('privacy-policy/', views.privacy_policy_page, name='policies'),
    path('privacy-policy/', views.privacy_policy_page, name='privacy_policy'),
    # path('terms-of-use/', views.terms_of_use_page, name='terms_of_use'),
    # path('cookies-policy/', views.cookies_policy_page, name='cookies_policy'),
    # path('data-rights/', views.data_rights_page, name='data_rights'),
    # path('security-policy/', views.security_policy_page, name='security_policy'),
]
