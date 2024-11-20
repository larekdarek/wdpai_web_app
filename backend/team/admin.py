from django.contrib import admin
from .models import TeamMember

# Rejestracja modelu TeamMember w panelu administracyjnym
admin.site.register(TeamMember)
