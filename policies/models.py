from django.db import models
from ckeditor.fields import RichTextField

class Policy(models.Model):
    POLICY_TYPES = (
        ('privacy', 'Privacy Policy'),
        ('terms', 'Terms of Use'),
        ('cookies', 'Cookies Policy'),
        ('data_rights', 'Data Rights'),
        ('security', 'Security Policy'),
    )
    
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES, unique=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Policies"
    
    def __str__(self):
        return self.get_policy_type_display()