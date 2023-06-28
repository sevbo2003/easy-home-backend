from django.contrib import admin
from apps.about.models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('years_of_experience', 'happy_clients', 'systems_installed')
