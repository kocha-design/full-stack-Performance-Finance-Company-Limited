# contact/models.py
from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=100)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return "Contact Information"

    class Meta:
        verbose_name_plural = "Contact Information"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']

       

class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="FontAwesome class e.g. 'fa fa-facebook'")

    def __str__(self):
        return f"{self.platform} - {self.url}"
