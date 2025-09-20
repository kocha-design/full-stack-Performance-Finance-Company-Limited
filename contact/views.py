# contact/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from contact.models import ContactInfo, ContactSubmission
from contact.forms import ContactForm

def contact(request):
    contact_info = ContactInfo.objects.first()  # Get the first ContactInfo record
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ujumbe wako umetumwa! Tutakujibu hivi karibuni.')
            return redirect('contact')
        else:
            messages.error(request, 'Tafadhali angalia fomu yako, kuna makosa.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'contact_info': contact_info})
from .models import SocialMedia

def social_media_links(request):
    return {
        'socialmedia_list': SocialMedia.objects.all()
    }
