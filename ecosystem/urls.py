from django.urls import path
from . import views

app_name = 'ecosystem'

urlpatterns = [
    path('', views.ecosystem_list, name='list'),
    path('<int:pk>/', views.ecosystem_detail, name='detail'),
    path('create/', views.ecosystem_create, name='create'),
    path('<int:pk>/update/', views.ecosystem_update, name='update'),
    path('<int:pk>/delete/', views.ecosystem_delete, name='delete'),
    path('<int:ecosystem_pk>/animals/create/', views.animal_create, name='animal_create'),
    path('animals/<int:pk>/update/', views.animal_update, name='animal_update'),
    path('animals/<int:pk>/delete/', views.animal_delete, name='animal_delete'),
]

