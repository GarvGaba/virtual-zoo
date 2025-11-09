from django.urls import path
from . import views

app_name = 'educational_sessions'

urlpatterns = [
    path('', views.session_list, name='list'),
    path('<int:pk>/', views.session_detail, name='detail'),
    path('create/', views.session_create, name='create'),
    path('<int:pk>/update/', views.session_update, name='update'),
    path('<int:pk>/delete/', views.session_delete, name='delete'),
    path('<int:pk>/enroll/', views.session_enroll, name='enroll'),
    path('<int:pk>/unenroll/', views.session_unenroll, name='unenroll'),
    path('<int:pk>/comment/', views.session_add_comment, name='add_comment'),
    path('<int:pk>/resource/', views.session_add_resource, name='add_resource'),
    path('<int:pk>/quiz/', views.session_add_quiz, name='add_quiz'),
]

