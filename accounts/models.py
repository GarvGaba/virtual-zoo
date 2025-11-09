from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with role-based authentication"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_admin_user(self):
        return self.role == 'admin' or self.is_superuser
    
    def is_teacher_user(self):
        return self.role == 'teacher'
    
    def is_student_user(self):
        return self.role == 'student'


class StudentProgress(models.Model):
    """Track student progress through ecosystems and sessions"""
    student = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='progress', limit_choices_to={'role': 'student'})
    ecosystem = models.ForeignKey('ecosystem.Ecosystem', on_delete=models.CASCADE, related_name='student_visits', null=True, blank=True)
    session = models.ForeignKey('educational_sessions.EducationalSession', on_delete=models.CASCADE, related_name='student_watches', null=True, blank=True)
    visited_at = models.DateTimeField(auto_now_add=True)
    time_spent_minutes = models.IntegerField(default=0, help_text="Time spent viewing in minutes")
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-visited_at']
        unique_together = [['student', 'ecosystem'], ['student', 'session']]
    
    def __str__(self):
        if self.ecosystem:
            return f"{self.student.username} visited {self.ecosystem.name}"
        return f"{self.student.username} watched {self.session.title}"
