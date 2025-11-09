from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class EducationalSession(models.Model):
    """Educational session model"""
    SESSION_TYPES = [
        ('workshop', 'Workshop'),
        ('lecture', 'Lecture'),
        ('interactive', 'Interactive'),
        ('field_trip', 'Virtual Field Trip'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES, default='lecture')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_sessions', limit_choices_to={'role': 'teacher'})
    ecosystem = models.ForeignKey('ecosystem.Ecosystem', on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')
    scheduled_date = models.DateTimeField()
    duration_minutes = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(180)])
    max_students = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to='sessions/', blank=True, null=True)
    hologram_preview = models.URLField(blank=True, null=True, help_text="URL to hologram preview")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-scheduled_date']
    
    def __str__(self):
        return f"{self.title} - {self.teacher.username}"


class SessionEnrollment(models.Model):
    """Student enrollment in educational sessions"""
    session = models.ForeignKey(EducationalSession, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments', limit_choices_to={'role': 'student'})
    enrolled_at = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['session', 'student']
        ordering = ['-enrolled_at']
    
    def __str__(self):
        return f"{self.student.username} - {self.session.title}"
