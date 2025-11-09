from django.contrib import admin
from .models import EducationalSession, SessionEnrollment, SessionResource, SessionComment, SessionQuiz


@admin.register(EducationalSession)
class EducationalSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'session_type', 'teacher', 'scheduled_date', 'duration_minutes', 'max_students']
    list_filter = ['session_type', 'scheduled_date', 'teacher']
    search_fields = ['title', 'description', 'teacher__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'scheduled_date'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'session_type', 'teacher', 'ecosystem')
        }),
        ('Schedule', {
            'fields': ('scheduled_date', 'duration_minutes', 'max_students')
        }),
        ('Content', {
            'fields': ('video_url', 'lesson_content', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(SessionResource)
class SessionResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'session', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title', 'session__title', 'description']


@admin.register(SessionComment)
class SessionCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'session', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'user__username', 'session__title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(SessionQuiz)
class SessionQuizAdmin(admin.ModelAdmin):
    list_display = ['question', 'session', 'correct_answer', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question', 'session__title']


@admin.register(SessionEnrollment)
class SessionEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['session', 'student', 'enrolled_at', 'attended']
    list_filter = ['attended', 'enrolled_at']
    search_fields = ['session__title', 'student__username']
    readonly_fields = ['enrolled_at']
