from .models import SocialMedia

def social_media_links(request):
    return {
        'socialmedia_list': SocialMedia.objects.all()
    }
