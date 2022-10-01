from django.shortcuts import render
from .models import Serial
from django.views.generic import ListView
from django.views.generic import DetailView

class SerialListView(ListView):
	template_name = 'serial_index.html'
	queryset = Serial.objects.all()
	context_object_name = 'serials'


class SerialDetailView(DetailView):

	template_name = 'serial_detail.html'
	queryset = Serial.objects.all()
	context_object_name = 'serial'