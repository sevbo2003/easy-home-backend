from django.contrib import admin
from apps.about.models import Experience, TeamMember


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('years_of_experience', 'happy_clients', 'systems_installed')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
