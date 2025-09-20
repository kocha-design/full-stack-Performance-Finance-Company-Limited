from django.db import models  # Hii lazima iwe kwanza

# Our Story
class Story(models.Model):
    title = models.CharField(max_length=200, default="Our Story")
    content = models.TextField()
    image = models.ImageField(upload_to="story/", blank=True, null=True)

    def __str__(self):
        return self.title

# Mission & Vision
class MissionVision(models.Model):
    TYPE_CHOICES = [
        ('mission', 'Mission'),
        ('vision', 'Vision')
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    content = models.TextField()

    def __str__(self):
        return self.type

# Core Values
class CoreValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

# Directors
class Director(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="directors/")

    def __str__(self):
        return self.name

# Stakeholders
class Stakeholder(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="stakeholders/")

    def __str__(self):
        return self.name
