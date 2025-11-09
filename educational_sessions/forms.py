from django import forms
from .models import EducationalSession, SessionResource, SessionComment, SessionQuiz


class EducationalSessionForm(forms.ModelForm):
    class Meta:
        model = EducationalSession
        fields = ['title', 'description', 'session_type', 'teacher', 'ecosystem', 'scheduled_date', 'duration_minutes', 'max_students', 'image', 'video_url', 'lesson_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'session_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'teacher': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'ecosystem': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'scheduled_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'max_students': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'video_url': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder': 'YouTube, Vimeo, or other video URL'}),
            'lesson_content': forms.Textarea(attrs={'rows': 6, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
        }


class SessionResourceForm(forms.ModelForm):
    class Meta:
        model = SessionResource
        fields = ['title', 'file', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'file': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
        }


class SessionCommentForm(forms.ModelForm):
    class Meta:
        model = SessionComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent', 'placeholder': 'Write your comment...'}),
        }


class SessionQuizForm(forms.ModelForm):
    class Meta:
        model = SessionQuiz
        fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'explanation']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 2, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'option_a': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'option_b': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'option_c': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'option_d': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'correct_answer': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
            'explanation': forms.Textarea(attrs={'rows': 2, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent'}),
        }

