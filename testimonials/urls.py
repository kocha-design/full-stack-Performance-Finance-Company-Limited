from django.urls import path
from . import views

app_name = "testimonials"

urlpatterns = [
    path("test/", views.testimonials_view, name="list"),  
]
