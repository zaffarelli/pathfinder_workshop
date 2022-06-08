from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Pathfinder Workshop Administration"
admin.site.site_title = "Pathfinder Workshop Administration Portal"
admin.site.index_title = "Welcome to the Pathfinder Workshop"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collector.urls')),
    path('', include('optimizer.urls')),
    path('', include('scenarist.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

