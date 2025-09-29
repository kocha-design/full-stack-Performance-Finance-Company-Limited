from django.shortcuts import render
from .models import Testimonial

def testimonials_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, "testimonials/testimonial.html", {"testimonials": testimonials})
