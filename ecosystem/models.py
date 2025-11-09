from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ecosystem(models.Model):
    """Ecosystem model for the Virtual Zoo"""
    REGION_CHOICES = [
        ('amazon', 'Amazon Rainforest'),
        ('sahara', 'Sahara Desert'),
        ('arctic', 'Arctic Tundra'),
        ('coral', 'Coral Reef'),
        ('savanna', 'African Savanna'),
        ('taiga', 'Boreal Forest (Taiga)'),
        ('temperate', 'Temperate Forest'),
        ('ocean', 'Deep Ocean'),
        ('mountain', 'Mountain Range'),
        ('wetland', 'Wetland'),
    ]
    
    ERA_CHOICES = [
        ('jurassic', 'Jurassic'),
        ('cretaceous', 'Cretaceous'),
        ('paleogene', 'Paleogene'),
        ('neogene', 'Neogene'),
        ('quaternary', 'Quaternary'),
        ('present', 'Present Day'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, default='amazon')
    era = models.CharField(max_length=50, choices=ERA_CHOICES, default='present')
    climate = models.CharField(max_length=100)
    temperature_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Minimum temperature in Celsius")
    temperature_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Maximum temperature in Celsius")
    vegetation = models.TextField(blank=True, help_text="Description of vegetation")
    precipitation = models.CharField(max_length=100, blank=True, help_text="Annual precipitation")
    image = models.ImageField(upload_to='ecosystems/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_ecosystems')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class Animal(models.Model):
    """Animal model within ecosystems"""
    SPECIES_TYPE_CHOICES = [
        ('existing', 'Existing Species'),
        ('extinct', 'Extinct Species'),
    ]
    
    ecosystem = models.ForeignKey(Ecosystem, on_delete=models.CASCADE, related_name='animals')
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    species_type = models.CharField(max_length=20, choices=SPECIES_TYPE_CHOICES, default='existing')
    description = models.TextField()
    habitat = models.CharField(max_length=200)
    diet = models.CharField(max_length=100)
    conservation_status = models.CharField(max_length=100, blank=True, help_text="e.g., Endangered, Least Concern, Extinct")
    image = models.ImageField(upload_to='animals/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.ecosystem.name})"
