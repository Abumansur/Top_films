import imp
from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import project_index, project_detail
from .views import ProjectDetailView, project_list
from .views import ProjectListView

urlpatterns = [
    path('', project_list, name='project_index'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
