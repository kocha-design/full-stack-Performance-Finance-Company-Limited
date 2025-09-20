from django.contrib import admin
from .models import GalleryImage

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order', 'created_date')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'created_date')
    search_fields = ('title', 'caption')
    
admin.site.register(GalleryImage, GalleryImageAdmin)