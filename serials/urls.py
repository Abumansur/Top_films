import imp
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SerialDetailView
from .views import SerialListView

urlpatterns = [
    path('', SerialListView.as_view(), name='serial_index'),
    path('<int:pk>/', SerialDetailView.as_view(), name='serial_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)