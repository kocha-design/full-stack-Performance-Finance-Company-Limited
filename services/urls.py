from django.urls import path
from . import views

app_name = 'services'  # namespace ya app

urlpatterns = [
    # path('', views.services_home, name='home'),  
    path('biashara/', views.biashara, name='biashara'),
    path('elimu/', views.elimu, name='elimu'),
    path('kilimo/', views.kilimo, name='kilimo'),
    path('nyumba/', views.nyumba, name='nyumba'),
    path('vikundi/', views.vikundi, name='vikundi'),
    path('waajiriwa/', views.waajiriwa, name='waajiriwa'),
    # path('',views.service_main, name='services'),
]
