from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import UserRegistrationForm
from .models import StudentProgress
from ecosystem.models import Ecosystem
from educational_sessions.models import EducationalSession, SessionEnrollment


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registration successful! Please login.')
        return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def student_dashboard(request):
    if not request.user.is_student_user():
        messages.error(request, 'Access denied. Student dashboard only.')
        return redirect('home')
    
    # Get student progress
    progress_ecosystems = StudentProgress.objects.filter(
        student=request.user,
        ecosystem__isnull=False
    ).select_related('ecosystem')
    
    progress_sessions = StudentProgress.objects.filter(
        student=request.user,
        session__isnull=False
    ).select_related('session')
    
    enrollments = SessionEnrollment.objects.filter(student=request.user).select_related('session')
    
    # Statistics
    total_ecosystems_visited = progress_ecosystems.count()
    total_sessions_watched = progress_sessions.count()
    total_enrollments = enrollments.count()
    total_time_spent = sum(p.time_spent_minutes for p in progress_ecosystems) + sum(p.time_spent_minutes for p in progress_sessions)
    
    return render(request, 'accounts/student_dashboard.html', {
        'progress_ecosystems': progress_ecosystems,
        'progress_sessions': progress_sessions,
        'enrollments': enrollments,
        'total_ecosystems_visited': total_ecosystems_visited,
        'total_sessions_watched': total_sessions_watched,
        'total_enrollments': total_enrollments,
        'total_time_spent': total_time_spent,
    })


@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher_user():
        messages.error(request, 'Access denied. Teacher dashboard only.')
        return redirect('home')
    
    # Get teacher's sessions
    sessions = EducationalSession.objects.filter(teacher=request.user)
    
    # Statistics
    total_sessions = sessions.count()
    total_enrollments = SessionEnrollment.objects.filter(session__teacher=request.user).count()
    upcoming_sessions = sessions.filter(scheduled_date__gte=timezone.now()).count()
    
    # Recent sessions
    recent_sessions = sessions.order_by('-created_at')[:5]
    
    return render(request, 'accounts/teacher_dashboard.html', {
        'sessions': sessions,
        'total_sessions': total_sessions,
        'total_enrollments': total_enrollments,
        'upcoming_sessions': upcoming_sessions,
        'recent_sessions': recent_sessions,
    })
