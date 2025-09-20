from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'categories', 'description')
    
    def save_model(self, request, obj, form, change):
        if obj.icon == "":
            obj.icon = None
        super().save_model(request, obj, form, change)

admin.site.register(Service, ServiceAdmin)
