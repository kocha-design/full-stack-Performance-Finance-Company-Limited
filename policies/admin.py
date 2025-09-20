from django.contrib import admin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_type', 'title', 'last_updated', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('policy_type', 'is_active')
    readonly_fields = ('last_updated',)
    
    fieldsets = (
        (None, {
            'fields': ('policy_type', 'title', 'content', 'is_active')
        }),
        ('Metadata', {
            'fields': ('last_updated',),
            'classes': ('collapse',)
        }),
    )