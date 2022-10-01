from django.shortcuts import render
from .models import Cartoon
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

class CartoonListView(ListView):
	template_name = 'cartoon_index.html'
	queryset = Cartoon.objects.all()
	context_object_name = 'cartoons'


class CartoonDetailView(DetailView):

	template_name = 'cartoon_detail.html'
	queryset = Cartoon.objects.all()
	context_object_name = 'cartoon'

