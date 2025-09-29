from django.shortcuts import render
from .models import GalleryImage
from testimonials.models import Testimonial
def home_page(request):
    testimonials = Testimonial.objects.all()  # leta testimonals zote
    gallery_images = GalleryImage.objects.all()
    
    context = {'gallery_images': gallery_images,
               'testimonials': testimonials
               }

    return render(request, 'home/home.html', context)
    
 
