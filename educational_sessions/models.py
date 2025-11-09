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
    video_url = models.URLField(blank=True, null=True, help_text="URL to video recording (YouTube, Vimeo, etc.)")
    lesson_content = models.TextField(blank=True, help_text="Additional lesson content/notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-scheduled_date']
    
    def __str__(self):
        return f"{self.title} - {self.teacher.username}"


class SessionResource(models.Model):
    """Downloadable resources for educational sessions"""
    session = models.ForeignKey(EducationalSession, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='session_resources/', help_text="PDF, notes, or other downloadable files")
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.title} - {self.session.title}"


class SessionComment(models.Model):
    """Comments on educational sessions"""
    session = models.ForeignKey(EducationalSession, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.session.title}"


class SessionQuiz(models.Model):
    """Quiz questions for educational sessions"""
    session = models.ForeignKey(EducationalSession, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200, blank=True)
    option_d = models.CharField(max_length=200, blank=True)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Session Quizzes'
    
    def __str__(self):
        return f"Quiz: {self.question[:50]}... - {self.session.title}"


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
