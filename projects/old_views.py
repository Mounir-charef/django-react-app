# from django.shortcuts import render, redirect
# from .forms import ProjectForm
# from .models import Project
#
#
# def projects(request):
#     all_project = Project.objects.all()
#     return render(request, template_name='index.html', context={
#         "data": all_project
#     })
#
#
# def project(request, pk):
#     projectObj = Project.objects.get(id=pk)
#     # tags = projectObj.tags.all()
#     # reviews = projectObj.review_set.all()
#
#     return render(request, 'project.html', context={"project": projectObj})
#
#
# def NewProject(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     form = ProjectForm()
#     context = {'form': form}
#     return render(request, 'project-form.html', context)
#
#
# def updateProject(request, pk):
#     altProject = Project.objects.get(id=pk)
#     form = ProjectForm(instance=altProject)
#     if request.method == 'POST':
#         print(request.headers)
#         form = ProjectForm(request.POST, instance=altProject)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     context = {'form': form}
#     return render(request, 'project-form.html', context)
#
#
# def deleteProject(request, pk):
#     prj = Project.objects.get(id=pk)
#     prj.delete()
#     return redirect('projects')
#
#
#
# # from django.contrib import admin
# # from django.urls import path, include
# #
# #
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('projects.urls'))
# # ]
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.projects, name="projects"),
#     path('project/<str:pk>/', views.project, name="project"),
#     path('add-project/', views.NewProject, name='create-project'),
#     path('alter-project/<str:pk>', views.updateProject, name='alter-project'),
#     path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
# ]
