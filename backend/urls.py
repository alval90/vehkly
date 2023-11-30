from django.contrib import admin
from django.shortcuts import render
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings

def index_view(request):
    return render(request, 'dist/index.html')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('api.urls')),
	re_path(r'^(?!api\/|media\/|admin\/).*$', index_view, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
