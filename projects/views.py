from django.shortcuts import render
from .models import Project 
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

class ProjectListView(ListView):
	template_name = 'project_index.html'
	queryset = Project.objects.all()
	context_object_name = 'projects'

def project_list(request):

	projects = Project.objects.all()
	context = {
		'projects':projects
	}
	return render(request, 'project_index.html', context)

#Стандартно в шаблоне -> object_list
"""def project_index(request):

	projects = Project.objects.all()
	context = {
		'projects': projects
	}
	return render(request, 'project_index.html', context)"""

class ProjectDetailView(DetailView):

	template_name = 'project_detail.html'
	queryset = Project.objects.all()
	context_object_name = 'project'

"""def project_detail(request, pk):

	project= Project.objects.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'project_detail.html', context)"""