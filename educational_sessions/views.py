from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from .models import EducationalSession, SessionEnrollment
from .forms import EducationalSessionForm


def session_list(request):
    sessions = EducationalSession.objects.filter(scheduled_date__gte=timezone.now())
    paginator = Paginator(sessions, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'educational_sessions/list.html', {'page_obj': page_obj})


def session_detail(request, pk):
    from .forms import SessionCommentForm, SessionResourceForm
    from accounts.models import StudentProgress
    
    session = get_object_or_404(EducationalSession, pk=pk)
    is_enrolled = False
    enrollment = None
    if request.user.is_authenticated and request.user.is_student_user():
        enrollment = SessionEnrollment.objects.filter(session=session, student=request.user).first()
        is_enrolled = enrollment is not None
        
        # Track student viewing
        progress, created = StudentProgress.objects.get_or_create(
            student=request.user,
            session=session,
            defaults={'completed': False}
        )
        if not created:
            progress.time_spent_minutes += 1
            progress.save()
    
    enrollments = session.enrollments.all()
    resources = session.resources.all()
    comments = session.comments.all()
    quizzes = session.quizzes.all()
    
    comment_form = SessionCommentForm() if request.user.is_authenticated else None
    
    return render(request, 'educational_sessions/detail.html', {
        'session': session,
        'is_enrolled': is_enrolled,
        'enrollment': enrollment,
        'enrollments': enrollments,
        'enrollment_count': enrollments.count(),
        'resources': resources,
        'comments': comments,
        'quizzes': quizzes,
        'comment_form': comment_form,
    })


@login_required
def session_create(request):
    if not (request.user.is_admin_user() or request.user.is_teacher_user()):
        messages.error(request, 'You do not have permission to create sessions.')
        return redirect('educational_sessions:list')
    
    if request.method == 'POST':
        form = EducationalSessionForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            if request.user.is_teacher_user():
                session.teacher = request.user
            session.save()
            messages.success(request, 'Educational session created successfully!')
            return redirect('educational_sessions:detail', pk=session.pk)
    else:
        form = EducationalSessionForm()
        if request.user.is_teacher_user():
            form.fields['teacher'].initial = request.user
    return render(request, 'educational_sessions/form.html', {'form': form, 'action': 'Create'})


@login_required
def session_update(request, pk):
    session = get_object_or_404(EducationalSession, pk=pk)
    if not (request.user.is_admin_user() or request.user == session.teacher):
        messages.error(request, 'You do not have permission to edit this session.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if request.method == 'POST':
        form = EducationalSessionForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Educational session updated successfully!')
            return redirect('educational_sessions:detail', pk=session.pk)
    else:
        form = EducationalSessionForm(instance=session)
    return render(request, 'educational_sessions/form.html', {'form': form, 'action': 'Update', 'session': session})


@login_required
def session_delete(request, pk):
    session = get_object_or_404(EducationalSession, pk=pk)
    if not (request.user.is_admin_user() or request.user == session.teacher):
        messages.error(request, 'You do not have permission to delete this session.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if request.method == 'POST':
        session.delete()
        messages.success(request, 'Educational session deleted successfully!')
        return redirect('educational_sessions:list')
    return render(request, 'educational_sessions/delete.html', {'session': session})


@login_required
def session_enroll(request, pk):
    session = get_object_or_404(EducationalSession, pk=pk)
    if not request.user.is_student_user():
        messages.error(request, 'Only students can enroll in sessions.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if SessionEnrollment.objects.filter(session=session, student=request.user).exists():
        messages.warning(request, 'You are already enrolled in this session.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if session.enrollments.count() >= session.max_students:
        messages.error(request, 'This session is full.')
        return redirect('educational_sessions:detail', pk=pk)
    
    enrollment = SessionEnrollment.objects.create(session=session, student=request.user)
    messages.success(request, f'Successfully enrolled in {session.title}!')
    return redirect('educational_sessions:detail', pk=pk)


@login_required
def session_unenroll(request, pk):
    session = get_object_or_404(EducationalSession, pk=pk)
    enrollment = SessionEnrollment.objects.filter(session=session, student=request.user).first()
    
    if not enrollment:
        messages.warning(request, 'You are not enrolled in this session.')
        return redirect('educational_sessions:detail', pk=pk)
    
    enrollment.delete()
    messages.success(request, f'Successfully unenrolled from {session.title}.')
    return redirect('educational_sessions:detail', pk=pk)


@login_required
def session_add_comment(request, pk):
    from .forms import SessionCommentForm
    
    session = get_object_or_404(EducationalSession, pk=pk)
    if request.method == 'POST':
        form = SessionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.session = session
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
    return redirect('educational_sessions:detail', pk=pk)


@login_required
def session_add_resource(request, pk):
    from .forms import SessionResourceForm
    
    session = get_object_or_404(EducationalSession, pk=pk)
    if not (request.user.is_admin_user() or request.user == session.teacher):
        messages.error(request, 'You do not have permission to add resources.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if request.method == 'POST':
        form = SessionResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.session = session
            resource.save()
            messages.success(request, 'Resource added successfully!')
    return redirect('educational_sessions:detail', pk=pk)


@login_required
def session_add_quiz(request, pk):
    from .forms import SessionQuizForm
    
    session = get_object_or_404(EducationalSession, pk=pk)
    if not (request.user.is_admin_user() or request.user == session.teacher):
        messages.error(request, 'You do not have permission to add quizzes.')
        return redirect('educational_sessions:detail', pk=pk)
    
    if request.method == 'POST':
        form = SessionQuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.session = session
            quiz.save()
            messages.success(request, 'Quiz question added successfully!')
    return redirect('educational_sessions:detail', pk=pk)
