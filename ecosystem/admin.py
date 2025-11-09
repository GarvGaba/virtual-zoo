from django.contrib import admin
from .models import Ecosystem, Animal


@admin.register(Ecosystem)
class EcosystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'era', 'location', 'climate', 'created_by', 'created_at']
    list_filter = ['region', 'era', 'climate', 'created_at']
    search_fields = ['name', 'description', 'location', 'vegetation']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'location', 'region', 'era')
        }),
        ('Environmental Data', {
            'fields': ('climate', 'temperature_min', 'temperature_max', 'vegetation', 'precipitation')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at')
        }),
    )


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name', 'species_type', 'ecosystem', 'diet', 'conservation_status', 'created_at']
    list_filter = ['ecosystem', 'species_type', 'diet', 'conservation_status', 'created_at']
    search_fields = ['name', 'scientific_name', 'description', 'habitat']
    readonly_fields = ['created_at', 'updated_at']
