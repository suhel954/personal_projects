from django.contrib import admin

# Register your models here.
from .models import Epidose

@admin.register(Epidose)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")
