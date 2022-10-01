import imp
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CartoonDetailView
#from .views import cartoons_list
from .views import CartoonListView

urlpatterns = [
    #path('', cartoons_list, name='cartoon_index'),
    path('', CartoonListView.as_view(), name='cartoon_index'),
    path('<int:pk>/', CartoonDetailView.as_view(), name='cartoon_detail'),
]
