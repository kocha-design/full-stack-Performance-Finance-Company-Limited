from django.shortcuts import render
from .models import GalleryImage

def home_page(request):
    gallery_images = GalleryImage.objects.all()
    context = {'gallery_images': gallery_images}
    return render(request, 'home/home.html', context)
