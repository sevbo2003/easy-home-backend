from django.db import models


class Experience(models.Model):
    years_of_experience = models.PositiveIntegerField()
    happy_clients = models.PositiveIntegerField()
    systems_installed = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team-members')
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        