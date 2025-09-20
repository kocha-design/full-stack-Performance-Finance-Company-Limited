from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')  # profile picture
    image = models.ImageField(upload_to='team/', blank=True, null=True)  # optional extra image
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Our Team"

    def __str__(self):
        return self.name
