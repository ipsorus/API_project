from django.contrib import admin
from api.models import Poverka

from django.contrib.admin import ModelAdmin


@admin.register(Poverka)
class PoverkaAdmin(ModelAdmin):
    pass
