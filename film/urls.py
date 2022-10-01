from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('hello_world.urls')),
    path('projects/', include('projects.urls')),
    path('cartoons/', include('cartoons.urls')),
    path('serials/', include('serials.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)