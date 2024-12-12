# mealshare/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # For media files
from django.conf.urls.static import static  # For media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('recipes.urls', namespace='recipes')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
