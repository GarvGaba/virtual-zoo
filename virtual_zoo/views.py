from django.shortcuts import render
from ecosystem.models import Ecosystem
from educational_sessions.models import EducationalSession
from django.utils import timezone


def home(request):
    featured_ecosystems = Ecosystem.objects.all()[:3]
    upcoming_sessions = EducationalSession.objects.filter(
        scheduled_date__gte=timezone.now()
    ).order_by('scheduled_date')[:3]
    
    return render(request, 'home.html', {
        'featured_ecosystems': featured_ecosystems,
        'upcoming_sessions': upcoming_sessions,
    })

