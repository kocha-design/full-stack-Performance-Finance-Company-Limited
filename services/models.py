from django.db import models

class Service(models.Model):
    SERVICE_TYPE = [
        ('biashara','biashara'),
        ('vikundi','vikundi'),
        ('nyumba','nyumba'),
        ('waajiriwa','waajiriwa'),
        ('kilimo','kilimo'),
        ('elimu','elimu'),
    ]

    title = models.CharField(max_length=200)
    categories =models.CharField(max_length=300, choices=SERVICE_TYPE, default='Select Category')
    description = models.TextField()
    # icon = models.ImageField(upload_to='services/', blank=True, null=True)
    icon = models.CharField(max_length=100, default='default-icon.png')

    def __str__(self):
        return self.title
