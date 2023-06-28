from django.db import models


class Experience(models.Model):
    years_of_experience = models.PositiveIntegerField()
    happy_clients = models.PositiveIntegerField()
    systems_installed = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        