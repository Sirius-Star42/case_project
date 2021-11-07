from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Marker

@admin.register(Marker)
class MarkerAdmin(OSMGeoAdmin):
    list_display = ('name', 'address', 'city', 'location')
