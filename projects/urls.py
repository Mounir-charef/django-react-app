from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.getProjects, name="projects"),
    path('projects/new/', views.createProject, name="projects"),
    path('project/<str:pk>/update/', views.updateProject, name="create-project"),
    path('project/<str:pk>/delete/', views.deleteProject, name="delete-project"),
    path('project/<str:pk>/', views.getProject, name="project"),
]
